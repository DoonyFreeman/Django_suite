from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<slug:category>/', views.product_category),
    

]