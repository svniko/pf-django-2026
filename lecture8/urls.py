from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="idex"),
    path("hello/", views.hello, name="index"),
    path("hello/<str:name>", views.hello_name, name="name"),
    path("hi/", views.hi, name="hi page with no name"),
    path("hi/<str:name>", views.hi, name="hi page"),
]