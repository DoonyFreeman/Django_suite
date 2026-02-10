from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_list(request):

    return HttpResponse("Страница со списком товаров")

def product_category(request, category):
    return HttpResponse(f"Категория {category}")