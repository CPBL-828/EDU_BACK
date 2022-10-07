from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TeacherView

teacher_list = TeacherView.as_view({
    'post': 'create',
    'get': 'list'
})

teacher_detail = TeacherView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('teacher/', teacher_list, name='teacher_list'),
    path('teacher/<int:pk>/', teacher_detail, name='teacher_detail'),
])