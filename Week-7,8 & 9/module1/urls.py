from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('hello1/', hello1, name="hello1"),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('print1/', print1, name='print1'),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('getdate1/', getdate1, name='getdate1'),
    path('get_date/', get_date, name='get_date'),
    path('registerlogin/', registerlogin, name='registerlogin'),
    path('registerloginfunction/', registerloginfunction, name='registerloginfunction'),
    path('pie/', pie, name='pie'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('travelservices/', travelservices, name='travelservices'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('feedback/', feedback, name='feedback'),
    path('feedbackform/', mainfeedback, name='mainfeedback'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('logout/', logout, name='logout'),

]

