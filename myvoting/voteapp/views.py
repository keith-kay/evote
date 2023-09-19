from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "index.html", context)

def detail(request, slug):
    category = Category.objects.get(slug=slug)
    context = {"category": category}
    return render(request, "detail.html", context)

def result(request):
    context = {}
    return render(request, "result.html", context)

def signin(request):
    context = {}
    return render(request, "signin.html", context)

def signup(request):
    
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login starts here
            username = request.POST['username'] 
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    context = {"form":form}
    return render(request, "signup.html", context)
