"""mymarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('carrinho/', views.carrinho),
    path('cadastrar/produto', views.cadastrar_produto),
    path('cadastrar/usuario', views.cadastrar_usuario),
    path('contato/', views.contato),
    path('parceiros/', views.parceiros),
    path('assinante/', views.assinante),
    path('localidades_atendidas/', views.localidades_atendidas),
    path('usuario/login', views.login),
    path('categoria/alimentos', views.cat_alimentos),
    path('categoria/bebidas', views.cat_bebidas),
    path('categoria/hortifruti', views.cat_hortifruti),
    path('categoria/utilitarios', views.cat_utilitarios),
    path('categoria/limpeza', views.cat_limpeza),
    path('categoria/higiene', views.cat_higiene),
    path('categoria/petshop', views.cat_pet),
    path('categoria/todos', views.cat_todos),
    path('produtos/todos', views.produtos_todos),
    path('fornecedores/', views.fornecedores),
    path('produto/<int:id>/', views.produtoView),
]





''' path('usuario/<str:name>', views.usuario, name='yourname'),'''
