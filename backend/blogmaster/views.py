from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

# Create your views here.
# Views are equivalent to routes in JavaScript


def main(reqeust):
    return HttpResponse("<h1>Hello</h1>")

@api_view(["POST"])
def signup(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    email = data['email']
    firstname = data['firstname']
    lastname = data['lastname']
    
    try:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
        user.save()
        
        return HttpResponse(json.dumps({'success': True}), content_type='application/json', status=200)
    except:
        # Return a failure response if the username is already taken
        return HttpResponse(json.dumps({'success': False}), content_type='application/json', status=400)



@api_view(["POST"])
def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        return HttpResponse(json.dumps({'success': True}), content_type='application/json', status=200)

    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json', status=400)

