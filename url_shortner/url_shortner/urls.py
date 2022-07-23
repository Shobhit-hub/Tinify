
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('email_verification.urls')),
    path('',include('short.urls')),
    path('<path:resource>',TemplateView.as_view(template_name='notavl.html'), name='notavl'),
    
   
]
