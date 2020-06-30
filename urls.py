from django.urls import path, include
from . import views 
from django.contrib import admin


urlpatterns = [
    path('', views.index, name="index"),
    path('registro', views.registro, name="registro"),
    path('estadistica', views.estadistica, name='estadistica'),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    
    path('admin/', admin.site.urls)
    
]
