from django.shortcuts import HttpResponse, redirect
from datetime import datetime

# Create your views here.

def hello_view(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')

def now_date(request):
    if request.method == "GET":
        return HttpResponse(datetime.now())

def goodbye(request):
    if request.method == "GET":
        return HttpResponse('Goodbye user')