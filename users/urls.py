from django.urls import path 
from users import views

urlpatterns = [path('', views.profile, name ="profile" ),
              path('login/', views.loginpage, name = "loginpage"), 
               path('logout/', views.logoutUser, name = "logoutuser"),
               path('register/', views.Registeruser, name = "Register"), 
               path('user-profile/<str:pk>', views.user, name= 'user-profile'),
               path('account/',views.useraccount, name = 'account' ),  
               path ('edit-profile/',views.editaccount, name= 'edit-profile' ),     
               path('deleteacc/',views.deleteacc, name = 'deleteacc'),                         
               path ('addskill/',views.addskills, name= 'addskills' ),                              
               path ('editskill/<str:pk>',views.editskill, name= 'editskills' ), 
               path ('deleteskill/<str:pk>',views.deleteskill, name= 'deleteskills' ), 
               path ('inbox/',views.inbox, name= 'inbox' ), 
            path ('messagecenter/<str:pk>/',views.messagecenter, name= 'messagecenter' ), 
              path ('sendmessage/<str:pk>/',views.sendmessage, name= 'sendmessage' ),
               ]