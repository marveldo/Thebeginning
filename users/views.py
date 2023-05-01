from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import Userupdatedform,Profileform,Skillform,MessageForm
from .models import Profile,Skill,Message
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .utils import searchprojects,pagination

# Create your views here.
def logoutUser(request):
    logout(request)
    messages.info(request, 'user has been logged out')
    return redirect('loginpage')
def Registeruser(request):
    page = 'register'
    form = Userupdatedform()
    if request.method == 'POST':
        form = Userupdatedform(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'account succesfully created')
            return redirect('loginpage')
            
    context = {'page': page , 'form': form}
    return render (request, 'users/login.html',context)

def loginpage(request):
    if request.user.is_authenticated :
        return redirect('profile')
    if request.method == 'POST' :
        username = request.POST['username'].lower()
        password = request.POST['password']
        try :
            user = User.objects.get(username = username)
        except :
            messages.error(request , 'User cannot be found')
        user = authenticate(request, username = username , password = password)    

        if user is not None :
            login(request,user) 
            messages.success(request, 'Login was succesful')
            return redirect (request.GET['next'] if 'next' in request.GET else 'account')
           
        else:
            messages.error(request, 'username or password is not correct')

    return render (request, 'users/login.html')

    

def profile(request):
    UserProfile , search = searchprojects(request)
    UserProfile,customrange ,paginator = pagination( request , UserProfile , 6)
   
    context = {'UserProfiles': UserProfile,'search':search , 'paginator':paginator, 'customrange': customrange}
    return render(request , 'users/profile.html', context )
def user(request, pk):
    user_profile = Profile.objects.get(id=pk)
    topskills = user_profile.skill_set.exclude(description__exact="")
    otherskills = user_profile.skill_set.filter(description = "")
    context = {'user_profile':user_profile,'topskills': topskills,'otherskills': otherskills}
    return render (request, 'users/user-profile.html',context)
@login_required(login_url="loginpage")
def useraccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all
    context = {'profile': profile , 'skills': skills } 
    return render (request, 'users/account.html',context)
def editaccount(request):
    acctprof = request.user.profile
    form = Profileform(instance = acctprof)
    if request.method == 'POST':
        form = Profileform(request.POST , request.FILES ,instance= acctprof ,)
        if form.is_valid():
            form.save()
            messages.success(request, 'account has been updated')
            return redirect('account')
        
    context = {'form': form, 'acctprof':acctprof }
    return render (request, 'users/edit-profile.html',context)
def addskills(request):
    profile = request.user.profile
    form = Skillform()
    if request.method == 'POST':
        form = Skillform(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.Owner = profile
            skill.save()
            messages.success(request, 'skill has been created')
            return redirect ('account')
    context = {'form': form}
    return render (request, 'users/skillform.html',context)
def editskill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = Skillform (instance = skill)
    if request.method == 'POST':
        form = Skillform(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request,'skill has been updated')
            return redirect ('account')
    context = {'form':form}
    return render(request, 'users/skillform.html',context)
def deleteskill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id =pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'skill has been deleted')
        return redirect('account')
    context = {'skill': skill}
    return render(request,'users/delete.html',context)
def inbox (request):
    profile = request.user.profile
    messagequery = profile.messages.all()
    unread_message = profile.messages.filter(is_read = False).count()
    context = {'messagequery':messagequery, 'unread_message': unread_message}
    return render (request,'users/inbox.html',context)
@login_required(login_url='loginpage')
def messagecenter(request,pk):
    profile = request.user.profile
    messagebox = profile.messages.get(id = pk)
    if messagebox.is_read == False :
        messagebox.is_read = True
        messagebox.save()
    context = {'messagebox': messagebox}
    return render (request,'users/message.html',context)

def sendmessage(request,pk ):
    userprofile = Profile.objects.get(id = pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
      form = MessageForm(request.POST)
      if form.is_valid():
           message = form.save(commit=False)
           message.sender = sender
           message.receiver = userprofile
           if sender:
               message.name = sender.username
               message.email = sender.email
           message.save()
           return redirect ('user-profile', userprofile.id )
    context = {'form':form}
    return render (request, 'users/sendmessage.html', context)
def deleteacc(request):
    profile = request.user.profile
    if request.method == 'POST':
        logout(request)
        profile.delete()
        
        messages.success(request,'Account has been deleted')
        return redirect('loginpage')
    context = {'profile':profile}
    return render (request,'users/deleteacc.html',context)
    