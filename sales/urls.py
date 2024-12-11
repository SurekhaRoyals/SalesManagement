from django.urls import path

from sales import views

urlpatterns = [
    path('',views.login_func, name = 'log'),
    path('signup/',views.signup_func, name = 'signup'),
    path('home/',views.home, name = 'home'),
    path('add/',views.addstudent, name = 'add'),
    path('display/',views.displaystudents, name = 'display'),
]