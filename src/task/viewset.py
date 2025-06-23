from .serializer import TaskLIstSerializer
from rest_framework import viewsets,mixins
from .models import TaskList,Task,Attachment


class TaskListViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset=TaskList.objects.all()
    serializer_class=TaskLIstSerializer
    permission_classes=[]