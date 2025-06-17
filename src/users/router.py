from rest_framework import routers
from .viewset import UserViewsets,ProfileViewSet

app_name="users"
router=routers.DefaultRouter()
router.register('users',UserViewsets)
router.register('profile',ProfileViewSet)
