#from django.contrib import admin
from django.urls import re_path

from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
]
