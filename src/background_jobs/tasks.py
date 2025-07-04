from background_task import background
from background_task.tasks import Task as BT
from house.models import House
from task.models import COMPLETE

@background(schedule=10)
def calculate_house_stats():
    for house in House.objects.all():
        total_tasks=0
        completed_task_count=0
        house_task_list=house.lists.all()
        for task_list in house_task_list():
            total_tasks +=task_list.tasks.count()
            completed_task_count += task_list.tasks.filter(status=COMPLETE).count()
            
            
        house.completed_tasks_count=completed_task_count
        house.notcompleted_tasks_count=total_tasks - completed_task_count
        house.save()


if not BT.objects.filter(verbose_name='calculate_house_stats').exists():
    calculate_house_stats(repeat=BT.DAILY, verbose_name='calculate_house_stats',priority=0)       