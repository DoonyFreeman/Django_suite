from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),       # Страница со списком товаров (catalog/)
    path('<slug:category>/', views.product_category),       # Категория товаров (catalog/something/)
    

]