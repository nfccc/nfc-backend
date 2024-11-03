from django.urls import path
from . import views

urlpatterns = [
    
path('bus-attendance/<str:bus_id>/', views.get_bus_attendance_by_date, name='get_bus_attendance_by_date'),


]
