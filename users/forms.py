from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile,Skill,Message

class Userupdatedform(UserCreationForm):
    class Meta :
        model = User 
        fields = ['first_name','username', 'email','password1','password2'] 
        labels = { 'first_name': 'Name',}
    def __init__(self,*args,**kwargs):
        super(Userupdatedform,self).__init__(*args,**kwargs)   
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
class Profileform(ModelForm):
    class Meta :
        model = Profile
        fields = ['name','bio','description','username','profile_pic','location']    
    def __init__(self,*args,**kwargs):
        super(Profileform,self).__init__(*args,**kwargs)   
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'}) 

class Skillform(ModelForm):
    class Meta :
        model = Skill  
        fields = '__all__'
        exclude = ['Owner']
    def __init__(self,*args,**kwargs):
        super(Skillform,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input' })
  
class MessageForm(ModelForm):
    class Meta :
        model = Message
        fields = ['name','subject','body','email'] 

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input' })