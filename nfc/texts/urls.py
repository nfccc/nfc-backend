# aifans/insights/urls.py
from django.urls import path
from . import views

# app_name = ''

urlpatterns = [
      path('test/', views.test_view, name='test_view'),
]
