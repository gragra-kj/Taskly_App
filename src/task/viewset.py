from .serializer import TaskLIstSerializer,TaskSerializer,AttachmentSerializer
from rest_framework import viewsets,mixins
from .models import TaskList,Task,Attachment
from .permissions import IsAllowedTOEditTaskListElseNone,IsAllowedToEdidTaskElseNone,IsAllowedToEditAttachmentElseNone


class TaskListViewset(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      #mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset=TaskList.objects.all()
    serializer_class=TaskLIstSerializer
    permission_classes=[IsAllowedTOEditTaskListElseNone,]
    
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAllowedToEdidTaskElseNone,]    
    
    def get_queryset(self):
        queryset=super(TaskViewSet,self).get_queryset()
        user_profile=self.request.user.profile
        updated_queryset=queryset.filter(created_by=user_profile)
        return updated_queryset
    
    
    
class AttachmentViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset=Attachment.objects.all()
    serializer_class= AttachmentSerializer
    permission_classes=[IsAllowedToEditAttachmentElseNone]   