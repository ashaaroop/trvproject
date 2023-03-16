
from . import views
from django.urls import path

import demo1app

urlpatterns = [

    path('',views.demofn,name='demofn'),

    # path('add/',views.addition,name='addition'),

]