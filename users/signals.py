import uuid
from users.models import Profile
from django.contrib.auth.models import User 
from django.db.models.signals import post_save,post_delete
from django.core.mail import send_mail
from django.conf import settings

def profileCreated(sender, instance , created, **kwargs):

    if created:
        user  =  instance
        profile =  Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email
                               )
        subject = 'welcome to devsearch'
        message = 'hope you have a good time'
        send_mail(
        subject ,
        message,
        settings.EMAIL_HOST_USER,
        [user.email]

            )
            
      
def profileupdated(sender,instance,created, **kwargs) :
    profile = instance
    user= profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deletinguser(sender , instance ,**kwargs) :
    user = instance.user
    user.delete()
    
    
     

post_save.connect(profileCreated, sender = User)
post_save.connect(profileupdated,sender = Profile)


post_delete.connect(deletinguser, sender = Profile)
