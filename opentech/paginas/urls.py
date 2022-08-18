from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('localizacao', views.localizacao, name='localizacao'),
    path('login', views.login, name='login'),
    path('servicos', views.servicos, name='servicos'),
    path('sobre', views.sobre, name='sobre'),
    path('vagas', views.vagas, name='vagas'),
]
