from django.shortcuts import render
# serializer 및 drf 사용
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializer 불러오기
from django.core import serializers
from . import serializers
from info.serializers import *
# 모델 불러오기
from .models import *
from members.models import *
# api_view 작성
from rest_framework.decorators import api_view
# JSON
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# 장고 모델 검색 기능
from django.db.models import Q
# 시간 관련 기능
import datetime


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


class AttendViewSet(viewsets.ModelViewSet):
    queryset = Attend.objects.all()
    serializer_class = AttendSerializer


attend_list = AttendViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

attend_detail = AttendViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


work_list = WorkViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

work_detail = WorkViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class SuggestViewSet(viewsets.ModelViewSet):
    queryset = Suggest.objects.all()
    serializer_class = SuggestSerializer


suggest_list = SuggestViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

suggest_detail = SuggestViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


consult_crud = ConsultViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

consult_detail = ConsultViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer


analysis_list = AnalysisViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

analysis_detail = AnalysisViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# 공지 리스트 검색 결과 반환
@api_view(['POST'])
def get_notice_list(request):
    try:
        # userKey 있는 지 확인
        if len(request.data["userKey"]) > 0:
            # 받은 userKey와 teacherKey와 매칭
            key = Teacher.objects.get(teacherKey=request.data["userKey"])
            # 강사키에 맞는 공지 리스트 정렬
            notice = list(Notice.objects.filter(readerKey=key).filter(
                Q(title__icontains=request.data['search']) |
                Q(content__icontains=request.data['search'])
            ).values())

            result = {'resultData': notice, 'count': len(notice)}

            return JsonResponse(result, status=200)

        else:
            data = list(Notice.objects.filter(type='전체').filter(
                Q(title__icontains=request.data['search']) |
                Q(content__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 건의 사항 리스트 필터링 및 반환
@api_view(['POST'])
def get_suggest_list(request):
    try:
        data = list(Suggest.objects.filter(
            state__icontains=request.data['search']).values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 상담 리스트 필터링 및 반환
@api_view(['POST'])
def get_consult_list(request):
    try:
        # userKey, studentKey 있는 지 확인
        if len(request.data['userKey']) > 0 and len(request.data['studentKey']) > 0:
            # 받은 userKey와 teacherKey와 매칭
            key = Teacher.objects.get(teacherKey=request.data['userKey'])
            # 유저키에 맞는 상담 리스트 정렬
            data = list(Consult.objects.filter(targetKey=key).
                        filter(studentKey=request.data['studentKey']).filter(
                Q(studentName__icontains=request.data['search']) |
                Q(consultType__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        # 유저키만 있을 때
        elif len(request.data['userKey']) > 0 and len(request.data['studentKey']) == 0:
            # 받은 userKey와 teacherKey와 매칭
            key = Teacher.objects.get(teacherKey=request.data['userKey'])
            # 상담 리스트 정렬
            data = list(Consult.objects.filter(targetKey=key).filter(
                Q(studentName__icontains=request.data['search']) |
                Q(consultType__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_consult_plan(request):
    try:
        serializer = ConsultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_consult(request):
    try:
        if Consult.objects.filter(consultKey=request.data['consultKey']).exists():

            consult = Consult.objects.get(consultKey=request.data['consultKey'])

            serializer = ConsultSerializer(consult, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_consult(request):
    try:
        if Consult.objects.filter(consultKey=request.data['consultKey']).exists():

            Consult.objects.filter(consultKey=request.data['consultKey']).update(editDate=datetime.datetime.now())

            consult = Consult.objects.get(consultKey=request.data['consultKey'])

            serializer = ConsultSerializer(consult, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def delete_consult(request):
    try:
        if Consult.objects.filter(consultKey=request.data['consultKey']).exists():

            time = Consult.objects.filter(consultKey=request.data['consultKey'])
            time.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)
