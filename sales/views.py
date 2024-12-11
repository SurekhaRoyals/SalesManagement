from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sales.models import Student
user1 = None


# Create your views here.
def login_func(request):
    global user1
    global user
    if request.method == "POST":
        name = request.POST["txtname"]
        email = request.POST["txtemail"]
        password = request.POST["txtpwd"]
        # global user
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_superuser:
                user1 = "admin"
                return render(request, 'home.html')

            elif user.is_authenticated:
                return render(request, 'home.html', {"sales":True, "user":user})
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
        if user1 == "admin":
             s1.sales_person_id = request.POST["sales_person"]
        else:
            s1.sales_person = user
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
    # if request.user.is_superuser:
    if user1 == "admin":
        students = Student.objects.all()
        return render(request, 'display.html', {"students":students, "salesperson":True, "update":True})
    else:
        print(user)
        students = Student.objects.filter(sales_person = user)
        return render(request, 'display.html', {"students": students, "salesperson":False, "update":False} )

def home(request):
    if user1 == "admin":
        return render(request, 'home.html')
    else:
        return render(request, 'home.html', {"sales" : True, "user": user})


# def update_student(request, id, student=None):
    users = User.objects.all()
    s1 = Student.objects.get(id = id)

    if request.method == "POST":
        if request.method == "POST":
            s1 = Student()
            if user1 == "admin":
                s1.sales_person_id = request.POST["sales_person"]
            else:
                s1.sales_person = user
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
        if user1 == "admin":
            users = Use.objects.all()
            return render(request, 'add.html', {"users":users})
        else:
            return render(request, 'add.html', {"salesperson" : False})

def delete_student(request, id):
    s1 = Student.objects.get(id = id)
    s1.delete()
    return redirect("display")