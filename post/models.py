from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
import uuid

class Pic(models.Model):
    image =models.ImageField(upload_to='photos')
    uuid = models.UUIDField(default= uuid.uuid4, editable= False, unique = True)
    def __str__(self):
        return str(self.image)
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted= models.DateTimeField(default=timezone.now)
    uploaded_by= models.ForeignKey(User,on_delete=models.CASCADE)
    image =  models.ManyToManyField(Pic)
    uuid = models.UUIDField(default= uuid.uuid4, editable= False, unique = True)
    def __str__(self):
        return str(self.uuid)


    