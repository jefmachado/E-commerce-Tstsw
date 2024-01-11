from django.urls import path
from django.contrib import admin
from appEcommerce import views



urlpatterns = [
    path('admin/',admin.site.urls),

    path('', views.Home, name='home'),

    path('produtos/',views.ProdutosCad, name='produtos'),

    path('listaprodutos/',views.Listaprodutos, name='listaprodutos'),

    path('editar/<int:id>', views.Editar, name='editar'),

    path('update/<int:id>', views.Update, name='update'),

    path('delete/<int:id>', views.Delete, name='delete'),

    path('busca/', views.Busca, name='busca'),
]
