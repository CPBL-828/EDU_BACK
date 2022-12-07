from django.urls import path, include
# viewsets을 router에 등록, URL 자동 생성
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notice', views.NoticeViewSet, basename='notice')
router.register(r'attend', views.AttendViewSet, basename='attend')
router.register(r'work', views.WorkViewSet, basename='work')
router.register(r'suggest', views.SuggestViewSet, basename='suggest')
router.register(r'consult', views.ConsultViewSet, basename='consult')
router.register(r'analysis', views.AnalysisViewSet, basename='analysis')

urlpatterns = [
    path('getNoticeList/', views.get_notice_list),
    path('getSuggestList/', views.get_suggest_list),
    path('getConsultList/', views.get_consult_list),
    path('createConsultPlan/', views.create_consult_plan),
    path('createConsult/', views.create_consult),
    path('editConsult/', views.edit_consult),
    path('deleteConsult/', views.delete_consult),
    path('getAnalysisList/', views.get_analysis_list),
    path('createAnalysis/', views.create_analysis),
    path('editAnalysis/', views.create_analysis),
    path('deleteAnalysis/', views.create_analysis),
    path('getAttendList/', views.get_attend_list),
    path('', include(router.urls)),
]
