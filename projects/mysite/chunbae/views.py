from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse("춘배의 고양이 세상")