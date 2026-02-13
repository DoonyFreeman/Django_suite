from django.urls import path
from . import views
app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),       # Страница со списком товаров (catalog/)
    path('<>/', views.product_category),       # Категория товаров (catalog/something/)
    path('<int:pk>/', views.product_detail, name='product_detail'),

]