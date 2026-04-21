from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup
# Create your views here.
def signup(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
      
        user = Signup(name=name, email=email, password=password)
        user.save()
    return render(request, "index.html")

def login(request):
    users = Signup.objects.all()
    return render(request, "home/login.html",{"users":users, "role":"manager"})   

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

#dsfsdfs