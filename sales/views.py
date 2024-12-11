from django.shortcuts import render

# Create your views here.
def login_func(request):
    return render(request,'login.html')


def signup_func(request):
    return render(request,'signup.html')