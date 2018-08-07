from django.contrib import admin
from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url('^$',indexView,name='register'),
    url('^answers/$',allAnswers,name='answers'),
    url('^administration/$',Administration,name='admin'),
    url('^question/(?P<pk>\d+)/$',Questions,name='question'),
    url('^answers/(?P<pk>\d+)/$',Answers,name='answer'),
    url('^results/$',results,name='results'),
    url('^search/$',admin_results,name='admin'),
    url('^list/(?P<pk>\d+)/$',list,name='list'),
    url('^variant/(?P<pk>\d+)/$',Variants,name='variant'),
    url('^choose/(?P<pk>\d+)/$',choose,name='choose'),
    url('^test/(?P<pk>\d+)/$',DetailView,name='detail'),
]
