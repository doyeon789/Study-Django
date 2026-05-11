from django.urls import path, include
from . import views

app_name = "articles"
urlpatterns = [
    path('index/', views.index, name='index'),
    path("dinner/", views.dinner, name='dinner'),
    path("search/", views.search, name='search'),
    path("throw/", views.throw, name='throw'),
    path("catch/", views.catch,name='catch'),
    path("articles/<int:num>", views.detail, name='detail'),
    path('company/', views.get_company_list, name='company'),
    path('intro_company/<str:company>/<str:name>', views.intro_company, name='intro_company')
]
