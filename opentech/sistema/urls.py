from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('cadastro/', views.cadastro_user, name='cadastro')
]