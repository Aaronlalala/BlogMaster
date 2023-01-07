from django.urls import path
# import main function
from . import views

urlpatterns =[
    path('signup', views.signup),
    path('login', views.login_action),
    path('logout', views.logout_action),
    path('create_post', views.create_post),
    path('delete_post/<int:pk>', views.delete_post),
    path('get_post/<int:pk>', views.get_post),
    path('create_comment', views.create_comment),
    path('get_comment/<int:pk>', views.get_comment),
    path('delete_comment/<int:pk>', views.delete_comment)
]