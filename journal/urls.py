# ~/projects/django-web-app/merchex/merchex/urls.py

from django.contrib import admin
from django.urls import path,include
from entree import views


urlpatterns = [
path('admin/', admin.site.urls),
path('home/', views.home, name="home"),
path('read/<int:idu>/<int:nbr>/',views.read,name="read"),
path('write/<int:idu>/', views.write, name="write"),
path('log/', views.log, name="log"),
path('sign/', views.sign, name="sign"),


]