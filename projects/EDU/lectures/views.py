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
from members.models import *
from lectures.models import *
from info.models import *
# api_view 작성
from rest_framework.decorators import api_view
# JSON
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# 장고 모델 검색 기능
from django.db.models import Q
# 쿼리셋 이름 변경
from django.db.models import F


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


class LectureStatusViewSet(viewsets.ModelViewSet):
    queryset = LectureStatus.objects.all()
    serializer_class = LectureStatusSerializer


lectureStatus_list = LectureStatusViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lectureStatus_detail = LectureStatusViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class AssignViewSet(viewsets.ModelViewSet):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer


assign_list = AssignViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

assign_detail = AssignViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


test_list = TestViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

test_detail = TestViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class TestStatusViewSet(viewsets.ModelViewSet):
    queryset = TestStatus.objects.all()
    serializer_class = TestStatusSerializer


testStatus_list = TestStatusViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

testStatus_detail = TestStatusViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


record_list = RecordViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

record_detail = RecordViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class PlannerViewSet(viewsets.ModelViewSet):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer


planner_list = PlannerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

planner_detail = PlannerViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# 강의실 검색 및 반환
@api_view(['POST'])
def get_lectureRoom_list(request):
    data = list(LectureRoom.objects.filter(
        Q(name__icontains=request.data['search']) |
        Q(type__icontains=request.data['search'])
    ).values())

    result = {'resultData': data, 'count': len(data)}

    return JsonResponse(result, status=200)


# 강의 목록 검색 및 반환
@api_view(['POST'])
def get_lecture_list(request):
    try:
        # userKey 있는 지 확인
        if len(request.data["userKey"]) > 0:
            # 받은 userKey와 teacherKey와 매칭
            key = Teacher.objects.get(teacherKey=request.data["userKey"])
            # 강사키에 맞는 강의 리스트 정렬
            lecture = list(Lecture.objects.filter(teacherKey=key).filter(
                Q(lectureName__icontains=request.data['search']) |
                Q(type__icontains=request.data['search']) |
                Q(subject__icontains=request.data['search']) |
                Q(target__icontains=request.data['search']) |
                Q(day__icontains=request.data['search'])
            ).values())

            result = {'resultData': lecture, 'count': len(lecture)}

            return JsonResponse(result, status=200)

        else:
            data = list(Lecture.objects.filter(
                Q(lectureName__icontains=request.data['search']) |
                Q(type__icontains=request.data['search']) |
                Q(subject__icontains=request.data['search']) |
                Q(target__icontains=request.data['search']) |
                Q(day__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_lecture_info(request):
    try:
        # userKey 있는 지 확인
        if len(request.data["userKey"]) > 0 and len(request.data["roomKey"]) > 0:
            # 받은 userKey와 teacherKey와 매칭
            key1 = Teacher.objects.get(teacherKey=request.data["userKey"])
            # 받은 roomKey와 roomKey와 매칭
            key2 = LectureRoom.objects.get(roomKey=request.data["roomKey"])
            # 정보 반환
            name = list(Teacher.objects.filter(teacherKey=key1).values('name'))
            room = list(LectureRoom.objects.filter(roomKey=key2).annotate(roomName=F('name')).values('roomName'))

            data = list(name + room)

            result = {'resultData': data}

            return JsonResponse(result, status=200)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_schedule_list(request):
    try:
        if len(request.data["roomKey"]) > 0:
            # 강의실 키에 맞는 강의키 정렬
            key = Lecture.objects.filter(roomKey=request.data['roomKey']).values('lectureKey')
            # 정렬한 강의키로 강의 리스트 정렬
            lecture = list(Lecture.objects.filter(lectureKey__in=key).values())

            result = {'resultData': lecture, 'count': len(lecture)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)
