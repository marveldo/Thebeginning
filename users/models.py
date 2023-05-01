from django.db import models
import uuid
from django.contrib.auth.models import User 
from django.db.models.signals import post_save,post_delete
from django.conf import settings
      # Create your models here.
class Profile(models.Model):
   user = models.OneToOneField(User ,  on_delete=models.CASCADE  )
 
                              
   name =  models.CharField(max_length=250, blank = True , null = True)
   email = models.EmailField(max_length=500, blank= True, null= True)
   bio =  models.CharField(max_length=500, blank=True, null=True)
   description = models.TextField(blank = True, null = True)
   username = models.CharField( blank = True,  null = True , max_length=160)
   profile_pic = models.ImageField(upload_to='user_profile' , default='default.jpeg', null = True , blank = True)
   location = models.CharField(max_length= 150, blank = True, null = True)
   created = models.DateTimeField(auto_now_add=True)
   id = models.UUIDField(default = uuid.uuid4, editable= False , unique= True, primary_key=True)

   class Meta:
       ordering = ['created']


   @property
   def ImageURL(self):
       try :
           url = self.profile_pic.url
       except : 
           url = settings.STATIC_URL + 'images/default.jpeg'
       return url
       
   
       
   def __str__(self):
       return str(self.username)
   

class Skill(models.Model):
    Owner = models.ForeignKey(Profile, blank= True, null = True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 75 , blank = True, null = True)
    description = models.TextField(max_length=250, null = True, blank = True )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, editable= False , unique= True, primary_key=True )
    
    def __str__(self):
        return self.name

class Message (models.Model):
    sender = models.ForeignKey(Profile, on_delete = models.SET_NULL , null = True, blank = True)
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL , related_name='messages' ,null = True, blank = True )
    name = models.CharField(max_length=200, blank = True,null = True)
    subject = models.CharField(max_length=200, blank = True,null = True)
    body = models.TextField()
    email = models.EmailField(max_length=200, blank = True,null = True)
    is_read = models.BooleanField(default=False , null = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, editable= False , unique= True, primary_key=True)

    def __str__(self):
        return self.subject