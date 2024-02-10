# In your_project/urls.py

from django.contrib import admin
from django.urls import path
from home.views import *  

urlpatterns = [
    path('login', home_view, name='home'), 
    path('', main_view,name="user"),
    path('get_my_reminders',get_reminders,name="my reminders"),
    path('save_content/',save_content,name="save content"),
    path('customer_list',customer_list,name="customer list")
]
