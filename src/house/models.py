from django.db import models
import os
#upload file
class GenerateHouseImagePath(object):
    def __init__(self):
        pass
    
    def __call__(self,instance,filename):
        ext=filename.split('.')[-1]
        path=f'media/house/{instance.id}/images'
        name=f'main.{ext}'
        return os.path.join(path,name)
        
house_image_path=GenerateHouseImagePath()        
        

# Create your models here.
class House(models.Model):
    name=models.CharField(max_length=120)
    image=models.FileField(upload_to=house_image_path,blank=True,null=True)