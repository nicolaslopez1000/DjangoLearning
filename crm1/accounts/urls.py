from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products),
    path('', views.home),
    path('customer/', views.customer),
]
