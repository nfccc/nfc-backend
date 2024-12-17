from django.urls import path, include
from rest import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserListCreateView, UserDetailView 
from django.contrib import admin
# from .views import VideoListCreateView
from .views import create_password, get_passwords
from .views import adverts_list, adverts_detail


schema_view = get_schema_view(
    openapi.Info(
        title="aifans",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('texts/', include('nfc.texts.urls')),
    path('track/', include('nfc.tag_id.urls')),
    path('students/', include('nfc.students.urls')),  # Connects students app URLs
    path('bus/', include('nfc.bus.urls')),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


