from django.urls import path
# import main function
from . import views

urlpatterns =[
    path('signup', views.signup),
    path('login', views.login),
    
]