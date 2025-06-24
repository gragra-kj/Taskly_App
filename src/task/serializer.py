from rest_framework import serializers
from .models import TaskList,Task,Attachment
from house.models import House


class TaskLIstSerializer(serializers.ModelSerializer):
    house=serializers.HyperlinkedRelatedField(queryset=House.objects.all(),many=False,view_name='house-detail')
    created_by=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    tasks=serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='task-detail')
    
    class Meta:
       model=TaskList
       fields=['created_on','completed_om','house','created_by','name','description','status','tasks']
       read_only_fields=['created_on','status']
       
class TaskSerializer(serializers.ModelSerializer):
    created_by=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    completed_on=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    task_list=serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(),many=False,view_name='tasklist-detail')
    attachments=serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='attachment-detail')
    
    def validate_tasklist(self,value):
        user_profile=self.context['request'].user.profile
        if value not in user.profile.house.list.all():
            raise serializers.ValidationError("Task list provided does not belong to house for which user is a member")
        return value
    
    def create(self, validated_data):
        user_profile=self.context['request'].user.profile
        task=Task.objects.create(**validated_data)
        task.created_by=user_profile
        task.save()
        return task
    
    class Meta:
        model=Task
        fields=['url','id','created_on','completed_on','created_by','completed_by','name','description','status','task_list','attachments']
        
        read_oly_fields=['created_on','created_by','completed_on','completed_by']       
        
        


class AttachmentSerializer(serializers.ModelSerializer):
    task=serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),many=False,view_name='task-detail')
    class Meta:
        model=Attachment
        fields=['id','url','created_on','data','task']
        read_only_fields=['created_on']        