from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Django. Lecture 8</h1>')

def hello(request):
    return HttpResponse('<h1>Hello</h1>')

def hello_name(request, name=None):
    return HttpResponse(f'<h1>Hello, {name.capitalize()}</h1>')

def hi(request, name=None):
    return render(request, 
                  'lecture8/index.html',
                  {'name':name}
                  )

