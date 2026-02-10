from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_list(request):              # Функция для обработки запроса на главную страницу каталога (catalog)

    return HttpResponse("Страница со списком товаров")

def product_category(request, category):            # Функция для обработки запроса на страницу категории товаров (catalog/something)
    return HttpResponse(f"Категория {category}")