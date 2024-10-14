from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Hello World, Hey Taohid What's up!</h1>")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("<h1>Hello World, this is about page</h1>")

def contact(request):
    return HttpResponse("<h1>Hello World, this contact page</h1>")