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
from datetime import datetime
# settings 불러오기
from config.settings import base


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


class PresenceViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer


presence_list = PresenceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

presence_detail = PresenceViewSet.as_view({
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
            # 강사키에 맞는 공지 리스트 정렬 (연도 검색이 있을 때 / 없을 때)
            if len(request.data['date']) == 0:
                notice = list(Notice.objects.filter(readerKey=key, type__icontains=request.data['type']).filter(
                    Q(title__icontains=request.data['search']) |
                    Q(content__icontains=request.data['search'])
                ).filter(createDate__year=datetime.now().year).order_by('-createDate').values())

                result = {'resultData': notice, 'count': len(notice)}

                return JsonResponse(result, status=200)

            else:
                notice = list(Notice.objects.filter(readerKey=key, createDate__icontains=request.data['date'],
                                                    type__icontains=request.data['type']).filter(
                    Q(title__icontains=request.data['search']) |
                    Q(content__icontains=request.data['search'])
                ).order_by('-createDate').values())

                result = {'resultData': notice, 'count': len(notice)}

                return JsonResponse(result, status=200)

        else:
            if len(request.data['date']) == 0:
                data = list(
                    Notice.objects.filter(type__icontains=request.data['type'])
                    .filter(Q(title__icontains=request.data['search']) |
                            Q(content__icontains=request.data['search'])
                            ).filter(createDate__year=datetime.now().year).order_by('-createDate').values())

                result = {'resultData': data, 'count': len(data)}

                return JsonResponse(result, status=200)

            else:
                data = list(
                    Notice.objects.filter(createDate__icontains=request.data['date'],
                                          type__icontains=request.data['type'])
                    .filter(Q(title__icontains=request.data['search']) |
                            Q(content__icontains=request.data['search'])
                            ).order_by('-createDate').values())

                result = {'resultData': data, 'count': len(data)}

                return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_notice(request):
    try:
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 건의 사항 리스트 필터링 및 반환
@api_view(['POST'])
def get_suggest_list(request):
    try:
        if request.data['userType'] == 'ADM':
            if request.data['writerType'] == 'STU':
                data = list(Suggest.objects.filter(writerType='STU').order_by('-createDate').values())

                result = {'resultData': data, 'count': len(data)}

                return JsonResponse(result, status=200)

            elif request.data['writerType'] == 'TEA':
                data = list(Suggest.objects.filter(writerType='TEA').order_by('-createDate').values())

                result = {'resultData': data, 'count': len(data)}

                return JsonResponse(result, status=200)

            elif request.data['writerType'] == 'PAR':
                data = list(Suggest.objects.filter(writerType='PAR').order_by('-createDate').values())

                result = {'resultData': data, 'count': len(data)}

                return JsonResponse(result, status=200)
        else:
            data = list(Suggest.objects.filter(writerKey=request.data['userKey']).order_by('-createDate').values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_suggest_plan(request):
    try:
        serializer = SuggestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_suggest_reply(request):
    try:
        if Suggest.objects.filter(suggestKey=request.data['suggestKey']).exists():

            suggest = Suggest.objects.get(suggestKey=request.data['suggestKey'])

            serializer = SuggestSerializer(suggest, request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                Suggest.objects.filter(suggestKey=request.data['suggestKey']).update(adminKey=request.data['adminKey'])
                Suggest.objects.filter(suggestKey=request.data['suggestKey']).update(state='Y')
                Suggest.objects.filter(suggestKey=request.data['suggestKey']).update(answerDate=datetime.now())

                result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_suggest(request):
    try:
        if Suggest.objects.filter(suggestKey=request.data['suggestKey']).exists():

            suggest = Suggest.objects.get(suggestKey=request.data['suggestKey'])

            serializer = SuggestSerializer(suggest, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Suggest.objects.filter(suggestKey=request.data['suggestKey']).update(editDate=datetime.now())

                result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def delete_suggest(request):
    try:
        if Suggest.objects.filter(suggestKey=request.data['suggestKey']).exists():

            suggest = Suggest.objects.filter(suggestKey=request.data['suggestKey'])
            suggest.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 상담 리스트 필터링 및 반환
@api_view(['POST'])
def get_consult_list(request):
    try:
        # userKey, studentKey 있는 지 확인
        if len(request.data['userKey']) > 0 and len(request.data['studentKey']) > 0:
            # 유저키에 맞는 상담 리스트 정렬
            data = list(
                Consult.objects.filter(targetKey=request.data['userKey'], consultDate__icontains=request.data['date']).
                filter(studentKey=request.data['studentKey']).filter(
                    Q(consultType__icontains=request.data['search'])
                ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        # 유저키만 있을 때
        elif len(request.data['userKey']) > 0 and len(request.data['studentKey']) == 0:
            # 상담 리스트 정렬
            data = list(Consult.objects.filter(targetKey=request.data['userKey'],
                                               consultDate__icontains=request.data['date']).filter(
                Q(consultType__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        elif len(request.data['userKey']) == 0 and len(request.data['studentKey']) > 0:
            data = list(Consult.objects.filter(studentKey=request.data['studentKey'],
                                               consultDate__icontains=request.data['date']).filter(
                Q(consultType__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            data = list(Consult.objects.all().values())

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

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

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

                result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_consult(request):
    try:
        if Consult.objects.filter(consultKey=request.data['consultKey']).exists():

            consult = Consult.objects.get(consultKey=request.data['consultKey'])

            serializer = ConsultSerializer(consult, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Consult.objects.filter(consultKey=request.data['consultKey']).update(editDate=datetime.now())

                result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def delete_consult(request):
    try:
        if Consult.objects.filter(consultKey=request.data['consultKey']).exists():

            consult = Consult.objects.filter(consultKey=request.data['consultKey'])
            consult.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_analysis_list(request):
    try:
        # userKey, studentKey 있는 지 확인
        if len(request.data['userKey']) > 0:
            key = Student.objects.get(studentKey=request.data['userKey'])

            data = list(Analysis.objects.filter(studentKey=key, createDate__icontains=request.data['date']).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_analysis(request):
    try:
        serializer = AnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_analysis(request):
    try:
        if Analysis.objects.filter(analysisKey=request.data['analysisKey']).exists():

            analysis = Analysis.objects.get(analysisKey=request.data['analysisKey'])

            serializer = AnalysisSerializer(analysis, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Analysis.objects.filter(analysisKey=request.data['analysisKey']).update(editDate=datetime.now())

                result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def delete_analysis(request):
    try:
        if Analysis.objects.filter(analysisKey=request.data['analysisKey']).exists():

            analysis = Analysis.objects.filter(analysisKey=request.data['analysisKey'])
            analysis.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_attend_list(request):
    try:
        if len(request.data['userKey']) > 0 and len(request.data['lectureKey']) > 0:
            try:
                if Student.objects.filter(studentKey=request.data['userKey']).exists():

                    attend = Attend.objects.filter(lectureKey=request.data['lectureKey']).filter(
                        studentKey=request.data['userKey']
                    ).values()

                    data = list(attend)

                    result = {'resultData': data, 'count': len(data)}

                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data['userKey']) == 0 and len(request.data['lectureKey']) > 0:
            try:
                if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():

                    attend = Attend.objects.filter(lectureKey=request.data['lectureKey']).values()

                    data = list(attend)

                    result = {'resultData': data, 'count': len(data)}

                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_attend(request):
    try:
        serializer = AttendSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_work_list(request):
    try:
        # userKey, studentKey 있는 지 확인
        if len(request.data['userKey']) > 0:
            key = Student.objects.get(studentKey=request.data['userKey'])

            data = list(Analysis.objects.filter(studentKey=key, createDate__icontains=request.data['date']).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_work(request):
    try:
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_presence_list(request):
    # required Key :  'date'
    try:
        if len(request.data['date']) > 0 and len(request.data['studentKey']) == 0:
            data = list(Presence.objects.filter(createDate__icontains=request.data['date']).order_by('-createDate').values())

            result = {'resultData': data, 'count': len(data)}
            return JsonResponse(result, status=200)

        elif len(request.data['date']) == 0 and len(request.data['studentKey']) > 0:
            data = list(Presence.objects.filter(studentKey=request.data['studentKey']).order_by('-createDate').values())

            result = {'resultData': data, 'count': len(data)}
            return JsonResponse(result, status=200)

        else:
            current_time = datetime.now().date()

            data = list(Presence.objects.filter(
                Q(createDate__year=current_time.year) &
                Q(createDate__month=current_time.month) &
                Q(createDate__day=current_time.day)
            ).order_by('-createDate').values())

            result = {'resultData': data, 'count': len(data)}
            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_presence(request):
    try:
        # 현재 시스템의 날짜와 시간을 가져오기
        current_date = datetime.now()
        # 현재 날짜의 요일 가져오기 (1: 월요일, 2: 화요일, ..., 7: 일요일)
        weekday = current_date.weekday() + 1
        # 연월일 비교하기
        current_time = datetime.now().date()
        # 중복 데이터 확인
        dup_date = Presence.objects.filter(
            Q(createDate__year=current_time.year) &
            Q(createDate__month=current_time.month) &
            Q(createDate__day=current_time.day)
        )

        if dup_date.exists():
            result = {'chunbae': '데이터가 이미 존재합니다.'}
            return JsonResponse(result, status=400)

        else:
            lecture = list(Lecture.objects.filter(day=weekday).values_list('lectureKey', flat=True))
            group = list(Lecture.objects.filter(lectureKey__in=lecture).values_list('groupKey', flat=True))
            student = list(GroupStatus.objects.filter(groupKey__in=group).values_list('studentKey', flat=True))

            data_list = []

            for i in student:
                item = {"studentKey": i}
                data_list.append(item)

            serializer = PresenceSerializer(data=data_list, many=isinstance(data_list, list))
            if serializer.is_valid():
                serializer.save()

                result = {'chunbae': '데이터 생성.', 'count': len(serializer.data)}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

@api_view(['POST'])
def edit_presence(request):
    try:
        presence = Presence.objects.get(studentKey=request.data['studentKey'])

        serializer = PresenceSerializer(presence, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            Presence.objects.filter(presenceKey=serializer.data['presenceKey']).update(editDate=datetime.now())

            result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)