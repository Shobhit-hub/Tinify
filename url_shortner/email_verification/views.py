from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from url_shortner.settings import base_address

def welcome(request):
    return render(request,'welcome.html')

def login_attempt(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.warning(request,"User not found")
            return redirect('/login')
        profile_obj=Profile.objects.filter(user=user_obj).first()
        if profile_obj.is_verified==False:
            messages.warning(request,"Profile is not verified,check mail")
            return redirect('/login')
        user=authenticate(username=username,password=password)
        if user is None:
            message=f'Wrong password'
            messages.warning(request,message)
            return redirect('/login')
        else:
            auth.login(request,user)
            return redirect('/')
            
    return render(request,'login.html')

def register_attempt(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
                messages.warning(request,'Username is taken')
                return redirect('/register')
            if User.objects.filter(email=email).first():
                messages.warning(request,'Email is taken')
                return redirect('/register')
            user_obj=User(username=username,email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token=str(uuid.uuid4())
            profile_obj=Profile.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email,auth_token)
            return redirect('/token')
        except Exception as e:
            print(e)
    return render(request,'register.html')

def success(request):
    return render(request,"success.html")
def token_send(request):
    return render(request,'token_send.html')
def verify(request,auth_token):
    try:
        profile_obj=Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.info(request,"Your profile is already verified")
                return redirect('/login')
            
        
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,'Congratulations!! Profile Verified')
            return redirect("/success")
        else:
            return redirect("/error")
    except Exception as e:
        print(e)        
            
def error_page(request):
    return render (request,'error.html')            

def send_mail_after_registration(email,token):
    subject="Your accounts need to be verified"
    message=f'Hi paste the link to verify {base_address}/verify/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)

def forgetPassword(request):
    try:
        if request.method=='POST':
            username=request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.warning(request,"No user found with this username")
                return redirect('/forget_password')
            
            user_obj=User.objects.get(username=username)
            profile_obj=Profile.objects.filter(user=user_obj).first()
            profile_obj.forget_password_token=str(uuid.uuid4())
            profile_obj.is_used=False
            profile_obj.save()
            try:
                send_mail_forget_password(user_obj.email,profile_obj.forget_password_token)
                messages.success(request,"Password Reset Email Sent")
            except Exception as e:
                print(e)
            return redirect('/forget_password')
    except Exception as e:
        print(e)
    return render(request,'forget_password.html')
def send_mail_forget_password(email,token):
    subject="Reset Password"
    message=f'Click on this link to reset password {base_address}/reset_password/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
def logout(request):
    auth.logout(request)
    return redirect('/')
def resetPassword(request,forget_password_token): 
    try:
        profile_obj=Profile.objects.filter(forget_password_token=forget_password_token).first()
        if profile_obj is None:
            return redirect("/error")
        if request.method=='POST':
            password=request.POST.get('password')
            
            if profile_obj:
                user_obj=profile_obj.user
                if profile_obj.is_used==False:
                    
                    
                    user_obj.set_password(password)
                    profile_obj.is_used=True   
                    profile_obj.save()
                    user_obj.save()
                    message=f'Password Reset successful'
                    messages.success(request,message)        
                else:
                    message =f'Link already used to reset password. Try generating link again. '
                    messages.warning(request,message)
            else:
                return redirect("/error")
    except Exception as e:
        print(e)  
    return render(request,'reset_password.html')