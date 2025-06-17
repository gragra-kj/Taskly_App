from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from .serialize import UserSerializer,ProfileSerializer
from .permissions import IsUserOwnerorGetandPostOnly,IsProfileOwnerOrReadOnly
from .models import Profile
class UserViewsets(viewsets.ModelViewSet):
    permission_classes=[IsUserOwnerorGetandPostOnly,]
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
class ProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    permission_classes=[IsProfileOwnerOrReadOnly,]
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer