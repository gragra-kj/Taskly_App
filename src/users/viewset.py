from django.contrib.auth.models import User
from rest_framework import viewsets
from .serialize import UserSerializer
from .permissions import IsUserOwnerorGetandPostOnly
class UserViewsets(viewsets.ModelViewSet):
    permission_classes=[IsUserOwnerorGetandPostOnly,]
    queryset=User.objects.all()
    serializer_class=UserSerializer