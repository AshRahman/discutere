from django.urls import path 
from .import views #This brings the urls from views file

urlpatterns = [
    path('', views.home, name= "home"),
    path('room/<str:pk>/', views.room, name="room"),
]