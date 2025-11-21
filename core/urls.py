from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('detalhe/<int:id>/', views.detalhe, name='detalhe'),
]
