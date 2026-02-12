from django.shortcuts import render
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader

def index(request):
    # Подключаем HTML-файл.
    template_name = 'homepage/index.html'
    title = 'Главная страница ACME'
    promo_product = 'Iron Carrot'
    context = {
        'title': title,
        'promo_product': promo_product,
    }
    # Передаём в объект HttpResponse 
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return render(request, template_name, context)