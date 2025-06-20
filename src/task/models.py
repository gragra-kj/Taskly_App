from django.db import models

# Create your models here.
COMPLETE= 'C'
NOT_COMPLETED='NC'
TASK_STATUS_CHOICE=[
    (NOT_COMPLETED,'Not completed'),
    (COMPLETE,'Completed')
    
]

class Task(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    completed_on=models.DateTimeField(null=True,blank=True)
    created_by=models.ForeignKey('users.Profile',null=True,blank=True,on_delete=models.SET_NULL,related_name='created_task')
    completed_by=models.ForeignKey('users.Profile',null=True,blank=True,on_delete=models.SET_NULL,related_name='compeletd_task')
    name=models.CharField(max_length=120)
    description=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=2,choices=TASK_STATUS_CHOICE,default=NOT_COMPLETED)
    
    def __str__(self):
        return {self.id} | {self.name}