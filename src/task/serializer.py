from rest_framework import serializers
from .models import TaskList
from house.models import House


class TaskLIstSerializer(serializers.ModelSerializer):
    house=serializers.HyperlinkedRelatedField(queryset=House.objects.all(),many=False,view_name='house-detail')
    created_by=serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    class Meta:
       model=TaskList
       fields=['created_on','completed_om','house','created_by','name','description','status']
       read_only_fields=['created_on','status']