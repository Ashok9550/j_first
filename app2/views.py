from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse('<h1>hello.....</h1>')
def hi(request):
    return HttpResponse('<marquee>second programe</marqee>')
