from django.shortcuts import render
from base.models import Room,tag
from base.forms  import Roomform,reviewform
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .utils import searchprojects,paginatepages

name = 'marvelous'


def room (request,pk):

     projectobj = Room.objects.get(id = pk)
     form = reviewform()
     if request.method == 'POST':
        
          form = reviewform(request.POST)
          if form.is_valid():
               review = form.save(commit = False)
               review.owner = request.user.profile
               review.room_name = projectobj
               review.save()
               projectobj.countvote
               return redirect('room', projectobj.id)
     context = {'project': projectobj,'form':form}    
    
     

     return render (request,'base/roompage.html',context,)
@login_required(login_url='loginpage')
def form (request) :
     profile = request.user.profile
     projects = Roomform()
     if request.method == 'POST':
          newtags = request.POST.get('Newtags').replace(',',' ').split()
          projects = Roomform(request.POST, request.FILES)
          if projects.is_valid():
               user =  projects.save(commit = False)
               user.owner = profile
               user.save()
               for tags in newtags:
                    tags,created = tag.objects.get_or_create(name=tags)
                    user.tags.add(tags)
               messages.success(request,'Project has been created')
                     
               return redirect ('account')
            
     context = {'projects': projects}
     return render( request, 'base/database.html',context)



def table (request) :
     room , search = searchprojects(request)
     room,pagerange,paginator = paginatepages(request,room,3)
     context = {'Room':room, 'search':search , 'paginator':paginator,'pagerange': pagerange}
     
     return render(request, 'base/table.html',context)
@login_required(login_url='loginpage')
def update (request,pk):
      profile = request.user.profile
      
      project =profile.room_set.get( id = pk)

     
           
      projects = Roomform( instance = project)
      
      if request.method == 'POST':
          newtags = request.POST.get('Newtags').replace(',',' ').split()
         
          projects = Roomform(request.POST, request.FILES ,instance = project)
          if projects.is_valid():
              project =  projects.save()
         
             
              for tags in newtags:
                  tags , created = tag.objects.get_or_create(name = tags)
                  project.tags.add(tags)
              project.save()
              messages.success(request,'project sucessfully updated')


              return redirect('table')
      context = {'projects': projects}
      return render( request, 'base/database.html',context)
@login_required(login_url='loginpage')
def  delete (request,pk):
     profile = request.user.profile
     projects =profile.room_set.get(id = pk)
     if request.method == 'POST':
          projects.delete()
          messages.success(request, 'project deleted successfully')
          return redirect('table')
          
     context = {'projects' : projects}   
     return render (request , 'base/quest.html', context)




              
     



   