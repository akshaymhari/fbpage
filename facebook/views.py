from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def fn_login(request):
    return render(request,'facebookHomePage.html')