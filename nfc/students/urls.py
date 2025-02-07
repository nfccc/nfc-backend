from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('all/', views.get_all_students, name='get_all_students'),
    path('class/<str:student_class>/', views.get_students_by_class, name='get_students_by_class'),
    path('edit/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete-all/', views.delete_all_students, name='delete_all_students'),  # ✅ New Route for Deleting All Students
    path('delete-by-name/<str:student_name>/', views.delete_student_by_name, name='delete_student_by_name'),
    path('nfc-scan/', views.handle_nfc_scan, name='handle_nfc_scan'),
]
