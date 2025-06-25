from .serializer import TaskLIstSerializer,TaskSerializer,AttachmentSerializer
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import viewsets,mixins,response
from rest_framework import status as s
from .models import TaskList,Task,Attachment,COMPLETE,NOT_COMPLETED
from .permissions import IsAllowedTOEditTaskListElseNone,IsAllowedToEdidTaskElseNone,IsAllowedToEditAttachmentElseNone
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status',]
        
    
    def get_queryset(self):
        queryset=super(TaskViewSet,self).get_queryset()
        user_profile=self.request.user.profile
        updated_queryset=queryset.filter(created_by=user_profile)
        return updated_queryset
    
    @action(detail=True,methods=['patch'])
    def update_task_status(self,request,pk=None):
        try:
            task=self.get_object()
            profile=request.user.profile
            status=request.data['status']
            if(status == NOT_COMPLETED):
                if(task.status == COMPLETE):
                    task.status=NOT_COMPLETED
                    task.completed_on=None
                    task.completed_by=None
                else:
                    raise Exception("Task already marked as not completed.")
                    
            elif(status==COMPLETE):
                if(task.status==NOT_COMPLETED):
                    task.status=COMPLETE
                    task.completed_on=timezone.now()
                    task.completed_by=profile
                else:
                    raise Exception("Task already marked as completed")    
            else:
                raise Exception("Incorrect status provided")
            task.save()
            serialzer=TaskSerializer(instance=task,context={'request':request})
            return response.Response(serialzer.data,status=s.HTTP_200_OK)
                
        except Exception as e:
            return response.Response({'detail':str(e)},status=s.HTTP_400_BAD_REQUEST)
            
        
    
    
    
class AttachmentViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset=Attachment.objects.all()
    serializer_class= AttachmentSerializer
    permission_classes=[IsAllowedToEditAttachmentElseNone]   