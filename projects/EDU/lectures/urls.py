from django.urls import path, include
# viewsets을 router에 등록, URL 자동 생성
from rest_framework.routers import DefaultRouter
from . import views

# DRF 라우터
router = DefaultRouter()
router.register(r'lectureRoom', views.LectureRoomViewSet, basename='notice')
router.register(r'lecture', views.LectureViewSet, basename='notice')

urlpatterns = [
   # path('getLectureRoomList/', views.get_lectureRoom_list),
   # path('getLectureList/', views.get_lecture_list),
   path('', include(router.urls)),
]