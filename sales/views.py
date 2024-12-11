from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sales.models import Student


# Create your views here.
def login_func(request):
    if request.method == "POST":
        name = request.POST["txtname"]
        email = request.POST["txtemail"]
        password = request.POST["txtpwd"]
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_superuser:
                return render(request, 'home.html')

            elif user.is_authenticated:
                return HttpResponse("Welcome to sales page")
            else:
                pass
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')


def signup_func(request):
    if request.method == "POST":
        name = request.POST["txtname"]
        email = request.POST["txtemail"]
        password = request.POST["txtpwd"]


        if User.objects.filter(Q(username = name) | Q(email = email)) & Q(password = password).exists():
            data = {"msg" : True}
            return render(request, 'signup.html')
        else:
            user1 = User.objects.create_user(username = name, email = email,password = password)
            user1.save()
            return redirect('log')



    else:
        return render(request,'signup.html')




def addstudent(request):
    if request.method == "POST":
        s1 = Student()
        s1.sales_person_id = request.POST["sales_person"]
        s1.joining_date = request.POST["txtdate"]
        s1.name = request.POST["txtname"]
        s1.age = request.POST["txtage"]
        s1.mobile = request.POST["txtmobile"]
        s1.email = request.POST["txtemail"]
        s1.education = request.POST["education"]
        s1.skills = request.POST["skills"]
        s1.save()
        return redirect('display')

    else:
        users = User.objects.all()
        return render(request, 'add.html',{"users":users})


def displaystudents(request):
    students = Student.objects.all()
    return render(request, 'display.html', {"students":students})


def home(request):
    return render(request, 'home.html')


def update_student(request, id):
    users = User.objects.all()
    s1 = Student.objects.get(id = id)

    if request.method == "POST":
        if request.method == "POST":
            s1 = Student()
            s1.sales_person_id = request.POST["sales_person"]
            s1.joining_date = request.POST["txtdate"]
            s1.name = request.POST["txtname"]
            s1.age = request.POST["txtage"]
            s1.mobile = request.POST["txtmobile"]
            s1.email = request.POST["txtemail"]
            s1.education = request.POST["education"]
            s1.skills = request.POST["skills"]
            s1.save()
            return redirect('display')
    else:
        return render(request, 'add.html', {"users":users, "student":student})


def delete_student(request, id):
    s1 = Student.objects.get(id = id)
    s1.delete()
    return redirect("display")