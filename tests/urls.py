from django.contrib import admin
from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url('^$',RegistrationView,name='register'),
    url('^login/$',Login,name='login'),
    url('^logout/$',Logout,name='logout',)
]
