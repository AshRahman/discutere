from django.contrib import admin
from django.urls import path, include # include works with views to bring the urls from core project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')), #this code brings in all the url from base/urls file

]
