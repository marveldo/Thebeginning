from django.db import models
import uuid
from users.models import Profile
from django.conf import settings

class Room (models.Model):
    owner = models.ForeignKey(Profile, null = True, blank =True , on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    
    featured_image = models.ImageField(null = True , blank = True , default= 'default.jpeg')
    about = models.TextField(null = True, blank = True)
    source_code = models.TextField(null = True, blank = True)
    tags = models.ManyToManyField('tag', blank = True ,)
    vote_total = models.IntegerField(default= 0 , null=True, blank = True)
    vote_ratio = models.IntegerField(default= 0 , null=True, blank = True)
    id = models.UUIDField(default = uuid.uuid4, editable= False , unique= True, primary_key=True)
    created = models.DateTimeField (auto_now_add= True)

    class Meta:
        ordering = ['-vote_ratio', '-vote_total','name']
    @property
    def  getreviewers(self):
        queryset = self.review_set.all().values_list('owner__id' , flat = True)
        return queryset
    @property
    def countvote(self):
        reviews = self.review_set.all()
        vote_count = reviews.filter(value ='up').count()
        total_vote =reviews.count()

        ratio = (vote_count/total_vote)*100

        self.vote_total = total_vote
        self.vote_ratio = ratio
        self.save()
    @property
    def ImageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = settings.STATIC_URL +'images/default.jpeg'
        return url


    def __str__(self):
        return self.name
class review (models.Model):
    vote = (
        ('up' , 'good review' ),
        ('bad',  'bad review')
    )
    owner = models.ForeignKey(Profile, on_delete = models.CASCADE , null = True)
    room_name = models.ForeignKey(Room , on_delete= models.CASCADE)
    description = models.TextField(null = True, blank = True)
    value = models.CharField(max_length=200, choices = vote)
    enjoyed = models.TextField(null = True, blank = True)
    id = models.UUIDField(default = uuid.uuid4,   unique= True, primary_key=True , editable= False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta :
        unique_together = [['owner' , 'room_name']]

    def __str__ (self):
        return self.value
class tag (models.Model):
     name = models.CharField(max_length=200)
     id = models.UUIDField(default = uuid.uuid4 ,unique= True, primary_key=True ,  editable= False)
     created = models.DateTimeField (auto_now_add= True)

     def __str__ (self):
        return self.name

# Create your models here.
