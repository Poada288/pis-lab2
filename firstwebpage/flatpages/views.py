from django.http import HttpResponse
from django.shortcuts import render


def hello_plain(request):
    return HttpResponse('Привет, Мир!', content_type='text/plain; charset=utf-8')


def hello(request):
    return HttpResponse('Привет, Мир!')


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'static_handler.html')
