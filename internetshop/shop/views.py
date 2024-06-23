from colorama import Fore
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (request):
    return HttpResponse('Hi, it is internet application!')