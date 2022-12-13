from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculus, name='derivative'),
    path('calculateNow', views.calculate, name='calculate')
]