from django.urls import path
# import main function
from . import views

urlpatterns =[
    path('signup', views.signup),
    path('login', views.login_action),
    path('logout', views.logout_action),
    path('create_post', views.create_post)
]