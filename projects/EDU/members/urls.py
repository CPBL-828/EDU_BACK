from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
])