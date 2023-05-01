from .models import Room,tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def searchprojects(request):
     search = ''
     if request.GET.get('search'):
          search = request.GET.get('search')
     tags = tag.objects.filter(name__iexact = search)
     room = Room.objects.distinct().filter(Q(name__icontains = search)|Q(owner__username__icontains = search)|Q(tags__in = tags))
     return (room ,search)
def paginatepages (request , room , rsults):
          page = request.GET.get('page')
          rsults =3
          paginator = Paginator(room,rsults)
          try:
             room = paginator.page(page)
         
          except PageNotAnInteger:
             page = 1
             room = paginator.page(page)
          except EmptyPage:
             page = paginator.num_pages     
             room = paginator.page(page)

     
          room = paginator.page(page)
          leftindex = int(page)- 1
          rightindex =int( page) +4
          if leftindex<1:
              leftindex = 1
          if rightindex > paginator.num_pages:
              rightindex = paginator.num_pages +1 
     
     
          pagerange = range(leftindex,rightindex)
          return(room,pagerange,paginator)