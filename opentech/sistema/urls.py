from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('cadastro/', views.cadastro_user, name='cadastro'),
    path('home/', views.home, name='home')

]