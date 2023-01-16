from django.urls import path, include
# viewsets을 router에 등록, URL 자동 생성
from rest_framework.routers import DefaultRouter
from . import views

# DRF 라우터
router = DefaultRouter()
router.register(r'lectureRoom', views.LectureRoomViewSet, basename='lectureRoom')
router.register(r'lecture', views.LectureViewSet, basename='lecture')
router.register(r'lectureStatus', views.LectureStatusViewSet, basename='lectureStatus')
router.register(r'assign', views.AssignViewSet, basename='assign')
router.register(r'test', views.TestViewSet, basename='test')
router.register(r'testStatus', views.TestStatusViewSet, basename='testStatus')
router.register(r'record', views.RecordViewSet, basename='record')
router.register(r'planner', views.PlannerViewSet, basename='planner')


urlpatterns = [
   path('getRoomList/', views.get_room_list),
   path('createRoom/', views.create_room),
   path('editRoom/', views.edit_room),
   path('deleteRoom/', views.delete_room),
   path('getLectureList/', views.get_lecture_list),
   path('getLectureInfo/', views.get_lecture_info),
   path('createLecturePlan/', views.create_lecture_plan),
   path('createLecture/', views.create_lecture),
   path('createPlanner/', views.create_planner),
   path('', include(router.urls)),
]