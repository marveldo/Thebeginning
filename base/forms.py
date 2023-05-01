from django.forms import ModelForm
from base.models import Room,review
from django import forms 

class Roomform (ModelForm):
    class Meta :
        model = Room
        fields = ['name','featured_image','about','source_code']

    def __init__(self,*args,**kwargs):
        super(Roomform,self).__init__(*args,**kwargs)   
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
class reviewform(ModelForm):
    class Meta :
        model = review
        fields = [ 'value' , 'description']
        labels = {'value': 'Place your vote',
            'description': 'Comment:' }

    def __init__(self,*args,**kwargs):
        super(reviewform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})