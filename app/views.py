from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    return HttpResponse('Vasyl Stefurak')

def age(request):
    return HttpResponse('14 years old')

def hobby(request):
    return HttpResponse('Learn python')
