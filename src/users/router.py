from rest_framework import routers
from .viewset import UserViewsets

app_name="users"
router=routers.DefaultRouter()
router.register('users',UserViewsets)