from django.urls import path
from . import views


# 지금 이 urls은 어떤 app이 관리하고 있는가?
app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
]
