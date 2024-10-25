# nfc/tag_id/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:tag_id>/', views.track_nfc_tag, name='track_nfc_tag'),
]
