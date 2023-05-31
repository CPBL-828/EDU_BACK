import shutil
from django.db.models import Func
# serializer 및 drf 사용
from rest_framework import viewsets
from rest_framework import status, generics
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
# 시간 관련 기능
import datetime
# settings 불러오기
from config.settings import base


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


class LectureStatusPlusViewSet(viewsets.ModelViewSet):
    queryset = LectureStatusPlus.objects.all()
    serializer_class = LectureStatusPlusSerializer


lectureStatusPlus_list = LectureStatusPlusViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lectureStatusPlus_detail = LectureStatusPlusViewSet.as_view({
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


class AssignStatusViewSet(viewsets.ModelViewSet):
    queryset = AssignStatus.objects.all()
    serializer_class = AssignStatusSerializer


assign_status_list = AssignStatusViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

assign_status_detail = AssignStatusViewSet.as_view({
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


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


group_list = RecordViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

group_detail = RecordViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class GroupStatusViewSet(viewsets.ModelViewSet):
    queryset = GroupStatus.objects.all()
    serializer_class = GroupStatusSerializer


groupStatus_list = GroupStatusViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

groupStatus_detail = GroupStatusViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# 강의실 검색 및 반환
@api_view(['POST'])
def get_room_list(request):
    ko_kr = Func(
        "name",
        function="ko_KR.utf8",
        template='(%(expressions)s) COLLATE "%(function)s"'
    )
    data = list(LectureRoom.objects.filter(
        Q(name__icontains=request.data['search']) |
        Q(type__icontains=request.data['search'])
    ).order_by(ko_kr.asc()).values())

    result = {'resultData': data, 'count': len(data)}

    return JsonResponse(result, status=200)


@api_view(['POST'])
def create_room(request):
    try:
        serializer = LectureRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def edit_room(request):
    try:
        if LectureRoom.objects.filter(roomKey=request.data['roomKey']).exists():

            room = LectureRoom.objects.get(roomKey=request.data['roomKey'])

            serializer = LectureRoomSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                LectureRoom.objects.filter(roomKey=request.data['roomKey']).update(editDate=datetime.datetime.now())

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
def delete_room(request):
    try:
        if LectureRoom.objects.filter(roomKey=request.data['roomKey']).exists():

            room = LectureRoom.objects.filter(roomKey=request.data['roomKey'])
            room.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 강의 목록 검색 및 반환
@api_view(['POST'])
def get_lecture_list(request):
    try:
        ko_kr = Func(
            "lectureName",
            function="ko_KR.utf8",
            template='(%(expressions)s) COLLATE "%(function)s"'
        )

        if len(request.data["userKey"]) > 0 and len(request.data['roomKey']) == 0:
            # 받은 userKey와 teacherKey와 매칭
            try:
                if Teacher.objects.filter(teacherKey=request.data['userKey']).exists():
                    key = Teacher.objects.get(teacherKey=request.data["userKey"])
                    # 강사키에 맞는 강의 리스트 정렬
                    lecture = list(Lecture.objects.filter(teacherKey=key).filter(
                        Q(lectureName__icontains=request.data['lectureName']) &
                        Q(roomName__icontains=request.data['roomName']) &
                        Q(target__icontains=request.data['target']))
                                   .order_by(ko_kr.asc()).values())

                    result = {'resultData': lecture, 'count': len(lecture)}

                    return JsonResponse(result, status=200)

                elif Student.objects.filter(studentKey=request.data["userKey"]).exists():
                    student = Student.objects.get(teacherKey=request.data["userKey"])

                    group = GroupStatus.objects.filter(studentKey=student)
                    lecture = LectureStatus.objects.filter(groupKey__in=group).values("lectureKey")

                    data = list(Lecture.objects.filter(lectureKey__in=lecture).values())

                    result = {'resultData': data, 'count': len(data)}

                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 : 데이터가 존재하지 않습니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        # 강의실 키가 있으면 강의실에 맞는 강의 리스트 반환
        elif len(request.data["userKey"]) > 0 and len(request.data['roomKey']) > 0:
            try:
                if LectureRoom.objects.filter(roomKey=request.data['roomKey']).exists():
                    # 강의실 키에 맞는 강의키 정렬
                    key = Lecture.objects.filter(roomKey=request.data['roomKey']).values('lectureKey')
                    # 정렬한 강의키로 강의 리스트 정렬
                    lecture = list(Lecture.objects.filter(lectureKey__in=key).filter(
                        Q(lectureName__icontains=request.data['lectureName']) &
                        Q(roomName__icontains=request.data['roomName']) &
                        Q(target__icontains=request.data['target']))
                                   .order_by(ko_kr.asc()).values())

                    result = {'resultData': lecture, 'count': len(lecture)}

                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 : 데이터가 존재하지 않습니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data["userKey"]) == 0 and len(request.data['roomKey']) > 0:
            try:
                if LectureRoom.objects.filter(roomKey=request.data['roomKey']).exists():
                    # 강의실 키에 맞는 강의키 정렬
                    key = Lecture.objects.filter(roomKey=request.data['roomKey']).values('lectureKey')
                    # 정렬한 강의키로 강의 리스트 정렬
                    lecture = list(Lecture.objects.filter(lectureKey__in=key).filter(
                        Q(lectureName__icontains=request.data['lectureName']) &
                        Q(roomName__icontains=request.data['roomName']) &
                        Q(target__icontains=request.data['target']))
                                   .order_by(ko_kr.asc()).values())

                    result = {'resultData': lecture, 'count': len(lecture)}

                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 : 데이터가 존재하지 않습니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data["userKey"]) == 0 and len(request.data['roomKey']) == 0:

            data = list(Lecture.objects.filter(
                Q(lectureName__icontains=request.data['lectureName']) &
                Q(roomName__icontains=request.data['roomName']) &
                Q(target__icontains=request.data['target']))
                        .order_by(ko_kr.asc()).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': 'key 확인 : 데이터가 존재하지 않습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 과거 시간표 조회 : 강의 마감일 - 등록일 사이 날짜에 입력값 날짜가 있을 시 반환
# teacherKey , date
@api_view(['POST'])
def get_past_lecture_list(request):
    try:
        if Teacher.objects.get(teacherKey=request.data['userKey']).exist():
            data = list(Lecture.objects.filter(teacherKey=request.data['userKey'],
                                               startDate__gte=request.data['date'],
                                               endDate__lte=request.data['data']).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': 'key 확인 : 데이터가 존재하지 않습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 강의 정보 반환 : 강사 이름 & 강의실 이름
@api_view(['POST'])
def get_lecture_info(request):
    try:
        ko_kr = Func(
            "lectureName",
            function="ko_KR.utf8",
            template='(%(expressions)s) COLLATE "%(function)s"'
        )
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
def get_lecture_status_list(request):
    try:
        ko_kr = Func(
            "name",  # 학생 모델 : name 필드
            function="ko_KR.utf8",
            template='(%(expressions)s) COLLATE "%(function)s"'
        )

        lecture = Lecture.objects.filter(lectureKey=request.data['lectureKey'])

        group_key = LectureStatusPlus.objects.filter(lectureKey=lecture)
        student_key = GroupStatus.objects.filter(groupKey__in=group_key).values('studentKey')

        data = list(Student.objects.filter(studentKey__in=student_key).order_by(ko_kr.asc()).values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_lecture_plan(request):
    try:
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_lecture(request):
    colors = {"국어": "#d57a7b", "수학": "#e39177", "영어": "#eeb958", "국사": "#80bdca",
              "탐구": "#678cbf", "특성화": "#a4a6d2", "논술": "#cc6699", "경시": "#e55c65",
              "SAT": "#e58a4e", "ACT": "#74c29a", "AP": "#5db7ad"}

    # total = list(LectureStatus.objects.filter(lectureKey=request.data['lectureKey']).values())

    try:
        if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():

            lecture = Lecture.objects.get(lectureKey=request.data['lectureKey'])

            serializer = LectureSerializer(lecture, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                subject = Lecture.objects.values_list('subject', flat=True).get(lectureKey=request.data['lectureKey'])
                total = LectureStatusPlus.objects.filter(lectuerKey=request.data['lectureKey'])

                Lecture.objects.filter(lectureKey=request.data['lectureKey']).update(color=colors[subject])
                Lecture.objects.filter(lectureKey=request.data['lectureKey']).update(total=total.count())

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
def create_lecture_status(request):
    try:
        serializer = LectureStatusPlusSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            print("data", request.data)
            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def edit_lecture_planner(request):
    try:
        if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():

            lecture = Lecture.objects.get(lectureKey=request.data['lectureKey'])
            planner = request.FILES.get('planner')
            old_planner = lecture.planner

            serializer = LectureSerializer(lecture, data=request.data, partial=True)

            if serializer.is_valid():
                # 강의 계획서 파일 처리
                if planner:
                    # 강의 계획서 파일 삭제
                    if old_planner:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_planner.name)
                        os.remove(old_file_path)

                    file_extension = planner.name.split('.')[-1]
                    file_name = f"{lecture}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, 'planner', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(planner.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, 'planner', planner.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT, 'planner', file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.planner.name = os.path.join('planner', file_name)
                    serializer.instance.save(update_fields=['planner'])
                else:  # 강의 계획서 파일을 삭제하는 경우
                    # 기존 강의 계획서 파일 삭제
                    if old_planner:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_planner.name)
                        os.remove(old_file_path)
                    serializer.instance.planner = None
                    serializer.instance.save(update_fields=['planner'])

                Lecture.objects.filter(lectureKey=request.data['lectureKey']).update(editDate=datetime.datetime.now())

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
def edit_lecture(request):
    try:
        if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():

            lecture = Lecture.objects.get(lectureKey=request.data['lectureKey'])
            # total = list(LectureStatus.objects.filter(lectureKey=lecture).values())

            serializer = LectureSerializer(lecture, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                total = LectureStatusPlus.objects.filter(lectuerKey=request.data['lectureKey'])
                Lecture.objects.filter(lectureKey=request.data['lectureKey']).update(total=total.count())
                Lecture.objects.filter(lectureKey=request.data['lectureKey']).update(editDate=datetime.datetime.now())

                result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def delete_lecture(request):
    try:
        if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():

            lecture = Lecture.objects.filter(lectureKey=request.data['lectureKey'])
            Lecture.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def get_assign_list(request):
    try:
        if Assign.objects.filter(lectureKey=request.data['lectureKey']).exists():
            data = list(Assign.objects.filter(lectureKey=request.data['lectureKey']
                                              ).order_by('deadLine').values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def get_assign_status_list(request):
    try:
        if AssignStatus.objects.filter(studentKeyKey=request.data['studentKey']).exists():
            data = list(AssignStatus.objects.filter(studentKey=request.data['studentKey']).order_by('studentName').values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': ' 데이터가 존재하지 않습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_assign(request):
    try:
        serializer = AssignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_assign_status(request):
    try:
        serializer = AssignStatusSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def edit_assign_file(request):
    try:
        if Assign.objects.filter(assignKey=request.data['assignKey']).exists():

            assign = Assign.objects.get(assignKey=request.data['assignKey'])
            assign_file = request.FILES.get('assignment')
            old_assign_file = assign.assignment

            serializer = AssignSerializer(assign, data=request.data, partial=True)

            if serializer.is_valid():
                # 강의 계획서 파일 처리
                if assign_file:
                    # 강의 계획서 파일 삭제
                    if old_assign_file:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_assign_file.name)
                        os.remove(old_file_path)

                    file_extension = assign_file.name.split('.')[-1]
                    file_name = f"{assign}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, 'assignment', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(assign_file.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, 'assignment', assign_file.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT, 'assignment', file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.assignment.name = os.path.join('assignment', file_name)
                    serializer.instance.save(update_fields=['assignment'])
                else:  # 강의 계획서 파일을 삭제하는 경우
                    # 기존 강의 계획서 파일 삭제
                    if old_assign_file:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_assign_file.name)
                        os.remove(old_file_path)
                    serializer.instance.assignment = None
                    serializer.instance.save(update_fields=['assignment'])

                Assign.objects.filter(assignKey=request.data['assignKey']).update(editDate=datetime.datetime.now())

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
def edit_assign(request):
    try:
        if Assign.objects.filter(assignKey=request.data['assignKey']).exists():

            assign = Assign.objects.get(assignKey=request.data['assignKey'])

            serializer = AssignSerializer(assign, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Assign.objects.filter(assignKey=request.data['assignKey']).update(editDate=datetime.datetime.now())

                result = {'chunbae': '데이터 수정.', 'resultData': serializer.data}
                return JsonResponse(result, status=201)
            else:
                result = {'chunbae': '수정 오류.', 'resultData': serializer.errors}
                return JsonResponse(result, status=400)

        else:

            return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def delete_assign(request):
    try:
        if Assign.objects.filter(assignKey=request.data['assignKey']).exists():

            assign = Assign.objects.filter(assignKey=request.data['assignKey'])
            assign.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def get_test_list(request):
    try:
        if Lecture.objects.filter(lectureKey=request.data['lectureKey']).exists():
            data = list(
                Test.objects.filter(lectureKey=request.data['lectureKey'], testType__icontains=request.data['type'],
                                    testDate__icontains=request.data['testDate']
                                    ).order_by('-createDate').values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def get_test_status_list(request):
    try:
        if Test.objects.filter(testKey=request.data['testKey']).exists():
            data = list(
                TestStatus.objects.filter(testKey=request.data['testKey']).order_by('studentName').values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            return JsonResponse({'chunbae': ' 데이터가 존재하지 않습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_test(request):
    try:
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_test_status(request):
    try:
        serializer = TestStatusSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def edit_test(request):
    try:
        if Test.objects.filter(testKey=request.data['testKey']).exists():

            test = Test.objects.get(testKey=request.data['testKey'])

            serializer = TestSerializer(test, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Test.objects.filter(testKey=request.data['testKey']).update(editDate=datetime.datetime.now())

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
def edit_test_sheet(request):
    try:
        if Test.objects.filter(testKey=request.data['testKey']).exists():

            test = Test.objects.get(testKey=request.data['testKey'])
            test_sheet = request.FILES.get('testSheet')
            old_test_sheet = test.testSheet

            serializer = TestSerializer(test, data=request.data, partial=True)

            if serializer.is_valid():
                # 강의 계획서 파일 처리
                if test_sheet:
                    # 강의 계획서 파일 삭제
                    if old_test_sheet:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_test_sheet.name)
                        os.remove(old_file_path)

                    file_extension = test_sheet.name.split('.')[-1]
                    file_name = f"{test}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, 'testSheet', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(test_sheet.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, 'testSheet', test_sheet.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT, 'testSheet', file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.testSheet.name = os.path.join('testSheet', file_name)
                    serializer.instance.save(update_fields=['testSheet'])
                else:  # 강의 계획서 파일을 삭제하는 경우
                    # 기존 강의 계획서 파일 삭제
                    if old_test_sheet:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_test_sheet.name)
                        os.remove(old_file_path)
                    serializer.instance.testSheet = None
                    serializer.instance.save(update_fields=['testSheet'])

                Test.objects.filter(testKey=request.data['testKey']).update(editDate=datetime.datetime.now())

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
def delete_test(request):
    try:
        if Test.objects.filter(testKey=request.data['testKey']).exists():

            test = Test.objects.filter(testKey=request.data['testKey'])
            test.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_group_list(request):
    try:
        ko_kr = Func(
            "groupName",
            function="ko_KR.utf8",
            template='(%(expressions)s) COLLATE "%(function)s"'
        )

        if request.data['userType'] == 'ADM':
            data = list(Group.objects.all().order_by(ko_kr.asc()).values())
            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        elif request.data['userType'] == 'TEA':
            teacher = Teacher.objects.get(teacherKey=request.data['teacherKey'])
            data = list(Group.objects.filter(teacherKey=teacher).order_by(ko_kr.asc()).values())
            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        elif request.data['userType'] == 'STU':
            student = Student.objects.get(studentKey=request.data['studentKey'])
            group = GroupStatus.objects.filter(studentKey=student).values('groupKey')
            data = list(Group.objects.filter(groupKey__in=group).order_by(ko_kr.asc()).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def get_group_status_list(request):
    try:
        ko_kr = Func(
            "name",
            function="ko_KR.utf8",
            template='(%(expressions)s) COLLATE "%(function)s"'
        )

        group = Group.objects.get(groupKey=request.data['groupKey'])

        student_key = GroupStatus.objects.filter(groupKey=group).values('studentKey')
        data = list(Student.objects.filter(studentKey__in=student_key).order_by(ko_kr.asc()).values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_group(request):
    try:
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def create_group_status(request):
    try:
        serializer = GroupStatusSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def edit_group(request):
    try:
        if Group.objects.filter(groupKey=request.data['groupKey']).exists():

            group = Group.objects.get(groupKey=request.data['groupKey'])

            serializer = GroupSerializer(group, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Group.objects.filter(groupKey=request.data['groupKey']).update(editDate=datetime.datetime.now())

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
def edit_group_status(request):
    try:
        group = Group.objects.get(groupKey=request.data[0]['groupKey'])
        GroupStatus.objects.filter(groupKey=group).delete()

        serializer = GroupStatusSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': ' key 확인 : 요청에 필요한 키를 확인해주세요.'}, status=400)


@api_view(['POST'])
def delete_group(request):
    try:
        if Group.objects.filter(groupKey=request.data['groupKey']).exists():

            group = Group.objects.filter(groupKey=request.data['groupKey'])
            group.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def delete_group_status(request):
    try:
        group = Group.objects.filter(groupKey=request.data['groupKey'])
        student = Student.objects.filter(studentKey=request.data['studentKey'])

        if group and student:

            groupStatus = GroupStatus.objects.filter(groupKey=group).filter(studentKey__in=student)
            groupStatus.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)
