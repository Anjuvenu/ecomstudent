from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logu, name='logu'),
    path('sign/', views.register, name='register'),
    path('product/', views.product, name='product'),
    path('category/', views.category, name='collection'),




]