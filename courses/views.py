from django.shortcuts import render, redirect
from .models import Course, Module
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,'base.html')

def course_detail(request,course_id):
    if request.user.is_authenticated:
        courses = Course.objects.get(id=course_id)
        title=courses.title
        modules = Module.objects.filter(course__title=title)
        return render(request,'course/course_list.html', dict(course=courses, modules=modules))
    else:
        messages.info(request, f"You are not logged in")
        return redirect(homepage)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created.")
            login(request, user)
            messages.info(request, f"You are logged in as {username}")
            return redirect(homepage)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = UserCreationForm
    return render(request, 'register.html', context={'form': form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect(homepage)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,f"You are logged in")
                return redirect(homepage)
            else:
                messages.error(request,f"Invalid Username and Password")
        else:
            messages.error(request, f"Invalid Username and Password")
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})