
from django.contrib import admin
from django.urls import path, include

from .views import *
urlpatterns = [
    path('',welcome,name="welcome"),
    path('login',login_attempt,name="login_attempt"),
    path('logout',logout,name='logout'),
    path('register',register_attempt,name="register_attempt"),
    path('token',token_send,name="token"),
    path('success',success,name="success"),
    path('forget_password',forgetPassword,name='forget_password'),
    path('verify/<auth_token>',verify,name="verify"),
    path('reset_password/<forget_password_token>',resetPassword,name="reset_password"),
    path('error',error_page,name="error"),
    
   # path('', include("apis.urls")),
]
