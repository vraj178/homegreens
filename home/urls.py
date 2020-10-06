from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalogue', views.catalogue, name='services'),
    path('contact', views.contact, name='contact'),
    ## Add
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout")
]
