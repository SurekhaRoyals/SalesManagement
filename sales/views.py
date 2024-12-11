from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_func(request):
    if request.method == "POST":
        name = request.POST["txtname"]
        email = request.POST["txtemail"]
        password = request.POST["txtpwd"]
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_superuser:
                return HttpResponse("Welcome to admin page")

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