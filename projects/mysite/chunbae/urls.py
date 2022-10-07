from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import TeacherViewSet

app_name = 'chunbae'

router = routers.DefaultRouter()
#router.register(r'teacher', TeacherViewSet, basename='Teacher')

urlpatterns = [
    # path('teacher/', include(router.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
