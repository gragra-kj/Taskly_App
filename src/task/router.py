from rest_framework import routers
from .viewset import TaskListViewset,TaskViewSet,AttachmentViewSet

app_name='task'
router=routers.DefaultRouter()
router.register('tasklist',TaskListViewset)
router.register('task',TaskViewSet)
router.register('attachment',AttachmentViewSet)