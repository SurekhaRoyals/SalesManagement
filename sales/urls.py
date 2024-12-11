from django.urls import path

from sales import views

urlpatterns = [
    path('',views.login_func),
    path('signup/',views.signup_func),
]