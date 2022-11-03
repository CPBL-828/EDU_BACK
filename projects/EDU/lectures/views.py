from django.shortcuts import render
# serializer 및 drf 사용
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializer 불러오기
from django.core import serializers
from . import serializers
from .serializers import *
# 모델 불러오기
from .models import *
# api_view 작성
from rest_framework.decorators import api_view
# JSON
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# 장고 모델 검색 기능
from django.db.models import Q


class LectureRoomViewSet(viewsets.ModelViewSet):
    queryset = LectureRoom.objects.all()
    serializer_class = LectureRoomSerializer


lectureRoom_list = LectureRoomViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lectureRoom_detail = LectureRoomViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


lecture_list = LectureViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lecture_detail = LectureViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
