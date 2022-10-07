from django.contrib import admin
from django.urls import path
from rest_framework import routers
from ninja import NinjaAPI
from . import views
from views import TestViewSet

app_name = 'chunbae'

api = NinjaAPI()

router = routers.DefaultRouter()
router.register('test', TestViewSet)


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('test', TestViewSet.as_view())
]
