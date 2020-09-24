from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"this is also sent"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def catalogue(request):
    return render(request,'catalogue.html')
    #return HttpResponse("this is service page")

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")