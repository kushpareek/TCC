from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('champion.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('Team_dashboard/', include(('Team_dashboard.urls', 'Team_dashboard'), namespace='Team_dashboard')),
    path('nexus/', include('nexus.urls')),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)