from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from djangoo import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def signup(request):
        if request.method=="POST":
            fname=request.POST['first_name']
            lname=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            pass1=request.POST['password']
            pass2=request.POST['confirm_password']
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return render(request,"authentication/index.html")
        
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, "Email Already Registered!!")
            #     return render(request,"authentication/index.html")
        
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return render(request,"authentication/index.html")
        
            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return render(request,"authentication/index.html")
        
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return render(request,"authentication/index.html")

            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
            subject = "Welcome to Portfolio-Chiragx._.17"
            message = "Hello " + myuser.first_name + "!! \n" + "Welcome to My website!! \nThank you for visiting\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            return redirect('signin')
        return render(request,"authentication/signup.html")
def signin(request):
    if request.method=="POST":
            username=request.POST['username']
            pass1=request.POST['password']
            user=authenticate(username=username,password=pass1)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged innn')
                return render(request,"authentication/fb.html")

            else:
                messages.error(request,'Username or password incorrect!')
                return redirect('signin')
    return render(request,"authentication/signin.html")

    return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
def fb(request):
    return render(request,"authentication/fb.html")
def ggl(request):
    return render(request,"authentication/ggl.html")
