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


# 공지 사항 모델 생성
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


notice_list = NoticeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

notice_detail = NoticeViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


@api_view(['POST'])
def get_notice_list(request):
    data = list(Notice.objects.filter(
        Q(title__icontains=request.data['search']) |
        Q(content__icontains=request.data['search'])
    ).values())

    result = {'resultData': data, 'count': len(data)}

    return JsonResponse(result, status=200)
