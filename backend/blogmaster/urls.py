from django.urls import path
# import main function
from .views import main

urlpatterns =[
    path('home', main)
]