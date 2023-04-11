from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('lectures/', include('lectures.urls')),
    path('info/', include('info.urls')),
]
