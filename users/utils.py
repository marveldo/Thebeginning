from .models import Profile,Skill
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def searchprojects (request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
    skills = Skill.objects.filter(name__iexact = search)
    UserProfile = Profile.objects.distinct().filter(Q(username__icontains = search)| Q(bio__icontains = search)| Q(skill__in = skills))

    return ( UserProfile, search)
def pagination(request, UserProfile ,results ):
     page = request.GET.get('page')
     results = 3
     paginator = Paginator(UserProfile, results)
     try:
       UserProfile = paginator.page(page)
     except PageNotAnInteger:
        page = 1
        UserProfile = paginator.page(page)
     except EmptyPage:
        page = paginator.num_pages
        UserProfile = paginator.page(page)
     leftindex = int(page)-1
     if leftindex <1:
        leftindex = 1
     rightindex = int(page) + 5
     if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages +1 
     customrange = range(leftindex,rightindex)
     UserProfile = paginator.page(page)
     return (UserProfile,customrange,paginator)