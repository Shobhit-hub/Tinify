from django.urls import path,include
from . import views
from .views import *
urlpatterns=[
    
    path('myurl',views.myurl,name='myurl'),
    path('random_url',views.random_url,name='random_url'),
    path('custom_url',views.custom_url,name='custom_url'),
    path('delete',views.delete1,name='delete'),
    path('update',views.update,name='update'),
    path('wanted',views.wanted,name='wanted'),
    path('help',help,name="help"),
    path('feedback',feedback,name="feedback"),
    path('urls/<str:iid>',views.redir,name='redir'),
    
]
