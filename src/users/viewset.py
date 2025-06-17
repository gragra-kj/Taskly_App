from django.contrib.auth.models import User
from rest_framework import viewsets
from .serialize import UserSerializer,ProfileSerializer
from .permissions import IsUserOwnerorGetandPostOnly
from .models import Profile
class UserViewsets(viewsets.ModelViewSet):
    permission_classes=[IsUserOwnerorGetandPostOnly,]
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer