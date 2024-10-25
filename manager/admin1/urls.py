from django.urls import path
from . import views

app_name = 'admin1'

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
]
