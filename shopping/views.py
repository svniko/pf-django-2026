from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

class NewItemForm(forms.Form):
    item = forms.CharField(label="New Item")

shop_list = ["bread", "butter", "cheese"]

def index(request):
    return render(request, "shopping/index.html",
                  {
                   "shop_list":shop_list,
                   "title":"Items"   
                  })

# def add(request):
#     if request.method == "POST":
#         item = request.POST.get('item')
#         shop_list.append(item)
#         return redirect("shopping:index")
#     return render(request, "shopping/add.html")

def add(request):
    if request.method == "POST":
        form  = NewItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]

            shop_list.append(item)

            # return redirect("shopping:index")
            return HttpResponseRedirect(reverse("shopping:index"))

    return render(request, "shopping/add.html", {
        "form":NewItemForm()
    })




