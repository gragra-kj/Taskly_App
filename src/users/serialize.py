from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model=User
        fields=['url','id','username','email','first_name','last_name']
        



