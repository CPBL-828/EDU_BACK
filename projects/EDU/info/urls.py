from django.urls import path, include
# viewsets을 router에 등록, URL 자동 생성
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notice', views.NoticeViewSet, basename='notice')

urlpatterns = [
   path('getNoticeList/', views.get_notice_list),
   path('', include(router.urls)),
]