from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"this is also sent"
    }
    if request.user.is_anonymous:
        return redirect ("/login")
    else:
        messages.success(request, "User Logged In")
        return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def catalogue(request):
    return render(request,'catalogue.html')
    #return HttpResponse("this is service page")

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")
#ADD
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        
        user=authenticate(username=username,password=password)
        print (user)
        if user is not None:
            print ('successful')
            login(request,user)
            return redirect("/")
        else:
            #not authroised
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    print("logging out")
    logout(request)
    print("ankesh")
    #print(user)
    return redirect("/")