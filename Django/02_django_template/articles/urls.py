from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'), 
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/<int:numm>/', views.detail, name='detail'),
    path('company_list/', views.get_company_list, name='get_company_list'),
    path('intro_company/<str:company>/<str:name>', views.intro_company, name='intro_company')
]
