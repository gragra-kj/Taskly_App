from django.contrib.auth.models import User
from rest_framework import viewsets
from .serialize import UserSerializer
class UserViewsets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer