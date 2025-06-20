from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct  import deconstructible
import os



@deconstructible
class GenerateProfileImagePath:
     def __init__(self):
          pass
     
     def __call__(self,instance,filename):
          ext=filename.split('.')[-1]
          path=f'media/accounts/{instance.user.id}/images/'
          name=f'profile_image{ext}'
 
          return os.path.join(path,name)
     
user_profile_path=GenerateProfileImagePath()     
# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     image=models.FileField(upload_to=user_profile_path,blank=True,null=True)
     house=models.ForeignKey('house.House',on_delete=models.SET_NULL,blank=True,null=True,related_name='members')
     
     def __str__(self):
          return f'{self.user.username}\'s Profile'
     
   
          
    