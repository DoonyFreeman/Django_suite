from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница') # Функция для обработки запроса на главную страницу (/)
# Create your views here.
