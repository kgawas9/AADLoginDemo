from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login_successful(request):
    return HttpResponse('Hey buddy, login successful.')