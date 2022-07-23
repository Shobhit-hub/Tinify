from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate
from django.contrib import messages,auth
from .models import *
from datetime import datetime, timedelta, timezone, tzinfo
from django.conf import settings
from django.core.mail import send_mail
from url_shortner.settings import base_address

from django.core.validators import URLValidator
validate = URLValidator()
import uuid


def random_url(request):
    if request.method=='POST':
        URL=myurls()
        URL.url=request.POST['url']
        try :
            validate(URL.url)
            URL.date=datetime.now()
            code_size=5
            loop_counter=0
            URL.uid=str(uuid.uuid4())[:code_size]
            
            while myurls.objects.filter(uid=URL.uid).exists():
                if loop_counter==5:
                    code_size+=1
                    loop_counter=0
                    delete_old()
                URL.uid=str(uuid.uuid4())[:code_size]
                loop_counter+=1
                
                    
            
            if request.user.is_authenticated:
                URL.username=request.user.username
            URL.save()
            messages.info(request,URL.url+'\nShortened to\n'+f'{base_address}/urls/'+URL.uid)
        except:
            messages.warning(request,"URL is invalid. URL format should be http://www.example.com/index.html")
        return redirect(random_url)
    else:
        f=myurls.objects.all()
        return render(request,'shorten.html',{'f':f})
def delete_old():
    
    for x in myurls.objects.filter(date__range=[datetime.now()-timedelta(days=180),datetime.now()-timedelta(days=30)] ):
        delete2(x.username,x.uid)
    
       
def custom_url(request):
    if request.method=='POST':
        URL=myurls()
        URL.url=request.POST['url']
        try :
            validate(URL.url)
            URL.date=datetime.now()
            URL.uid=request.POST['code']
            for ch in URL.uid:
                if ch.isalnum()==0:
                    messages.warning(request,"Code must be alphanumeric")
                    return redirect(custom_url)
            
            
            if len(URL.uid)>200:
                messages.warning(request,"code too long please make it under 200")
                return redirect(custom_url)
            if myurls.objects.filter(uid=URL.uid).exists():
                messages.warning(request,"Already in use , please try a different code")
                return redirect(custom_url)
            if request.user.is_authenticated:
                URL.username=request.user.username
            URL.save()
            for wanted_obj in imp_urls.objects.filter(uid=URL.uid):
                wanted_obj.target=URL.url
                wanted_obj.save()
            imp_urls.objects.filter(uid=URL.uid,username=request.user.username).delete()
            messages.info(request,URL.url+'\nShortened to\n'+f'{base_address}/urls/'+URL.uid)
        except:
            messages.warning(request,"URL is invalid. URL format should be http://www.example.com/index.html")
        return redirect(custom_url)
    else:
        f=myurls.objects.all()
        return render(request,'shorten0.html',{'f':f})
def redir(request,iid):
    URL=myurls.objects.filter(uid=iid)
    for X in URL:
        X.date=datetime.now()
        X.save();
        return redirect(X.url)
        
    return render(request,'free.html')

# def main1(request):
#     return render(request,'main.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def myurl(request):
    if request.user.is_authenticated:
        f=myurls.objects.filter(username=request.user.username)
        return render(request,'myurl.html',{'f':f})
    return render(request,'notavl.html')
    
        
def delete1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            try:
                
                code=request.POST['code']
                
                for wanted_obj in imp_urls.objects.filter(uid=code):
                    wanted_obj.target=""
                    user_obj=User.objects.filter(username=wanted_obj.username).first()
                    send_mail_available(user_obj.email,code)
                    wanted_obj.save()
                myurls.objects.filter(username=request.user.username,uid=code).delete()
                messages.success(request,"URL deleted")
            except:
                messages.warning(request,"Please select a url")
            return redirect('/delete')
        else:
            f=myurls.objects.filter(username=request.user.username)
            return render(request,'deletemyurl.html',{'f':f})
    return render(request,'notavl.html')
def delete2(username,code):
    for wanted_obj in imp_urls.objects.filter(uid=code):
        wanted_obj.target=""
        user_obj=User.objects.filter(username=wanted_obj.username).first()
        send_mail_available(user_obj.email,code)
        wanted_obj.save()
    myurls.objects.filter(username=username,uid=code).delete()
    #messages.success(request,"URL deleted")
    # return render(request,'notavl.html')
    #return redirect('http://127.0.0.1:8000/delete')
def send_mail_available(email,code):
    subject="Code Available"
    message=f'Code {code} is available now . Click this link to aquire it!! {base_address}/custom_url'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)

def update(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            try:
                uid=request.POST['uid']
            except:
                messages.warning(request,"Please select a url")
                return redirect('/update')
            try :
                new_url=request.POST['new_url']
                validate(new_url)
                record=myurls.objects.filter(username=request.user.username,uid=uid)
                for rec in record:
                    rec.url=request.POST['new_url']
                    rec.save()
                for wanted_obj in imp_urls.objects.filter(uid=uid):
                    wanted_obj.target=new_url
                wanted_obj.save()
                messages.success(request,"URL updated")
            except:
                messages.warning(request,'URL not valid')
            return redirect('/update')
        else:
            f=myurls.objects.filter(username=request.user.username)
            return render(request,'updatemyurl.html',{'f':f})
    return render(request,'notavl.html')
def wanted(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            
            uid=request.POST['uid']
            if len(uid)>200:
                messages.warning(request,"code too long please make it under 200")
                return redirect(wanted)
            if myurls.objects.filter(uid=uid).exists():
                
                if myurls.objects.filter(uid=uid,username=request.user.username).exists():
                    messages.warning(request,"This code belongs to you, try update")
                    return redirect(update)
                else :
                    cur=imp_urls.objects.filter(uid=uid,username=request.user.username)
                    
                    if imp_urls.objects.filter(uid=uid,username=request.user.username).exists():
                        
                        
                        messages.warning(request,"Code already in list")
                        return redirect(wanted)
                    else:
                        user_obj=myurls.objects.filter(uid=uid).first();
                        target=user_obj.url
                        imp=imp_urls(uid=uid,target=target,username=request.user.username)
                        imp.save()
                        messages.success(request,'Code added')
                    
            else:
                messages.success(request,"Code is not in use you can have it!")
                return redirect("/custom_url")
        for imp_obj in imp_urls.objects.filter():
            cur=myurls.objects.filter(uid=imp_obj.uid)
            if(cur is None):
                imp_obj.url="";
                imp_obj.save();
        f=imp_urls.objects.filter(username=request.user.username)
        return render(request,'wanted.html',{'f':f})
    return render(request,'notavl.html')

def feedback(request):
    if request.method=='POST':
        comments=request.POST['comments']
        feedback=user_feedback(username=request.user.username,comments=comments)
        feedback.save()
        messages.success(request,"feedback saved")
        return redirect("/feedback")
    return render(request,'feedback.html')
