from django.http import HttpResponse

def home(reqest):
    return HttpResponse("Hello, world! This is the home page of the first project.")

def about(reqest):
    return HttpResponse("Hello, world! This is the about page of the first project.")

def contact(reqest):
    return HttpResponse("Hello, world! This is the contact page of the first project.")