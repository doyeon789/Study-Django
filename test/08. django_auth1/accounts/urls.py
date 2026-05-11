from django.urls import path
from . import views

app = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login')
]