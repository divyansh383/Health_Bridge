from django.urls import path
from . import views

from artEfact.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView 
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path('api',views.api),
    path('addReport',views.setSymptoms),
    path('getReport',views.getReports)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)