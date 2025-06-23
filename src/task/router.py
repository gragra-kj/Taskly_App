from rest_framework import routers
from .viewset import TaskListViewset

app_name='task'
router=routers.DefaultRouter()
router.register('tasklist',TaskListViewset)