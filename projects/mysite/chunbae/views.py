from django.shortcuts import render
import json  # json데이터를 파이썬 딕셔너리로 변환
from django.http import HttpResponse
from django.http import JsonResponse  # 파이썬 딕셔너리 JSON 변환, 프론트응답
from django.views import View  # view기능이 담긴 모듈
from rest_framework import viewsets
from .serializer import TeacherSerializer
from .models import Teacher
import datetime


def index(request):
    cM = 120
    sH = datetime.datetime.strptime("18:10", '%H:%M').hour
    sM = datetime.datetime.strptime("18:10", '%H:%M').minute

    time = (sH * 60) + sM + cM

    eH = str(int(time / 60))
    eM = str(int(time % 60))
    return HttpResponse(eH + ":" + eM)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
