from rest_framework import serializers
from .models import TaskList,Task,Attachment
from house.models import House


class TaskLIstSerializer(serializers.ModelSerializer):
    house=serializers.HyperlinkedRelatedField(queryset=House.objects.all(),many=False,view_name='house-detail')
    created_by=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    class Meta:
       model=TaskList
       fields=['created_on','completed_om','house','created_by','name','description','status']
       read_only_fields=['created_on','status']
       
       
class TaskSerializer(serializers.ModelSerializer):
    created_by=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    completed_on=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    task_list=serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(),many=False,view_name='tasklist-detail')
    class Meta:
        model=Task
        fields=['url','id','created_on','completed_on','created_by','completed_by','name','description','status','task_list']
        read_oly_fields=['created_on','created_by','completed_on','completed_by']       
        


class AttachmentSerializer(serializers.ModelSerializer):
    task=serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),many=False,view_name='task-detail')
    class Meta:
        model=Attachment
        fields=['id','url','created_on','data','task']
        read_only_fields=['created_on']        