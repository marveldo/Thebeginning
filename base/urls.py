from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.table, name="table" ),
    path('room/<str:pk>/',views.room, name = "room"),
    path('room/form',views.form, name = "form"),

    path('forms/update/<str:pk>/', views.update, name = "update"),
    path('delete/<str:pk>/', views.delete, name = "delete"),
    
    
]

