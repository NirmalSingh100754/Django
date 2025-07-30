from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! This is the home page of the first project.")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello, world! This is the about page of the first project.")

def contact(request):
    return HttpResponse("Hello, world! This is the contact page of the first project.")