from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.settings import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('lectures/', include('lectures.urls')),
    path('info/', include('info.urls')),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
