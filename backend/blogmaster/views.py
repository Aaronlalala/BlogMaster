from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views are equivalent to routes in JavaScript


def main(reqeust):
    return HttpResponse("<h1>Hello</h1>")