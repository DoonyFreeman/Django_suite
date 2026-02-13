from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_list(request):              # Функция для обработки запроса на главную страницу каталога (catalog)
    template_name = 'catalog/product_list.html'
    title = 'Список товаров ACME'
    products = [
        'Iron carrot',
        'Giant mousetrap',
        'Dehydrated boulders',
        'Invisible paint',
    ]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, template_name, context)

def product_category(request, category):            # Функция для обработки запроса на страницу категории товаров (catalog/something)
    return HttpResponse(f"Категория {category}")

def product_detail(request, pk):            # Функция для обработки запроса на страницу товара (catalog/123)
    if pk == 1:
        template_name = 'catalog/product_detail.html'
        title = 'Страница товара ACME'
        context = {
            'title': title
        }
        return render(request, template_name, context)
    else:
        return HttpResponse(f"Страница товара {pk} не найдена")