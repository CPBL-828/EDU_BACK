# serializer 및 drf 사용
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializer 불러오기
from django.core import serializers
from . import serializers
from .serializers import *
# 모델 불러오기
from .models import *
from info.models import *
# api_view 작성
from rest_framework.decorators import api_view
# JSON
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# 장고 모델 검색 기능
from django.db.models import Q


# CUSTOM model 에 대한 view
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # 로그인 인증된 요청에 한해 view 호출 허용


teacher_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

teacher_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


admin_list = AdminViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

admin_detail = AdminViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


student_list = AdminViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

student_detail = AdminViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


parent_list = AdminViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

parent_detail = AdminViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# 로그인 로직
@api_view(['POST'])
def compare(request):
    # user_type -> 강사: TEA, 관리자: ADM, 학생: STU, 학부모: PAR
    user_type = request.data['userType']
    # 수신 데이터 data에 저장
    data = request.data['id']

    global ident, info, info_json

    if user_type == 'TEA':

        queryset = Teacher.objects.all()
        serializer_class = TeacherSerializer

        try:
            if (Teacher.objects.filter(id=data)).exists():
                # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Teacher.objects.get(id=data)
                # Teacher 모델 id=data인 데이터 조회
                info = Teacher.objects.filter(id=data)
                # ident 값 serializer를 통해 json 파싱 / queryset => json
                info_json = TeacherSerializer(ident)

            else:
                return JsonResponse({'chunbae': '강사 정보가 존재하지 않습니다.'}, status=400)
        except KeyError:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    elif user_type == 'ADM':

        queryset = Admin.objects.all()
        serializer_class = AdminSerializer

        try:
            if (Admin.objects.filter(id=data)).exists():
                # Admin 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Admin.objects.get(id=data)
                # Admin 모델 id=data인 데이터 조회
                info = Admin.objects.filter(id=data)
                # Admin 값 serializer를 통해 json 파싱 / queryset => json
                info_json = AdminSerializer(ident)

            else:
                return JsonResponse({'chunbae': '관리자 정보가 존재하지 않습니다'}, status=400)
        except KeyError:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    elif user_type == 'STU':

        queryset = Student.objects.all()
        serializer_class = StudentSerializer

        try:
            if (Student.objects.filter(id=data).values()).exists():
                # Student 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Student.objects.get(id=data)
                # Student 모델 id=data인 데이터 조회
                info = Student.objects.filter(id=data)
                # ident 값 serializer를 통해 json 파싱 / queryset => json
                info_json = StudentSerializer(ident)

            else:
                return JsonResponse({'chunbae': '학생 정보가 존재하지 않습니다'}, status=400)
        except KeyError:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    elif user_type == 'PAR':

        queryset = Parent.objects.all()
        serializer_class = ParentSerializer

        try:
            if (Parent.objects.filter(id=data)).exists():
                # Parent 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Parent.objects.get(id=data)
                # Parent 모델 id=data인 데이터 조회
                info = Parent.objects.filter(id=data)
                # Parent 값 serializer를 통해 json 파싱 / queryset => json
                info_json = ParentSerializer(ident)

            else:
                return JsonResponse({'chunbae': '학생 정보가 존재하지 않습니다'}, status=400)
        except KeyError:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        ident = Parent.objects.get(id=data)
        info = Parent.objects.filter(id=data)
        info_json = ParentSerializer(ident)

    try:
        if info.exists():
            # ident는 키를 반환, 해당 키를 가진 모델의 id 필드값과 data 비교
            if ident.id == data:
                # {'ensure_ascii' : False} => json 문자열이 한글로 표시되도록
                return JsonResponse(info_json.data, json_dumps_params={'ensure_ascii': False}, status=200)
            else:
                return JsonResponse({'message': '주인님이 아니시군요?'}, status=400)
        else:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 학생 리스트 반환
@api_view(['POST'])
def get_student_list(request):
    try:
        # userKey 있는 지 확인
        if len(request.data["userKey"]) > 0:
            # 받은 userKey와 teacherKey와 매칭
            key = Teacher.objects.get(teacherKey=request.data["userKey"])
            # 강사키에 맞는 강의 리스트 정렬 : 중복 강의명 제거)
            lecture = Lecture.objects.filter(teacherKey=key).values('lectureKey').distinct('name')
            # 강의키에 맞는 학생 리스트 정렬
            student = LectureStatus.objects.filter(lectureKey__in=lecture).values('studentKey')
            # 학생 리스트 생성 : 검색 기능 포함
            data = list(Student.objects.filter(studentKey__in=student).filter(
                Q(name__icontains=request.data['search']) |
                Q(school__icontains=request.data['search']) |
                Q(grade__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

        else:
            data = list(Student.objects.filter(
                Q(name__icontains=request.data['search']) |
                Q(school__icontains=request.data['search']) |
                Q(grade__icontains=request.data['search'])
            ).values())

            result = {'resultData': data, 'count': len(data)}

            return JsonResponse(result, status=200)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_student(request):
    try:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


# 강사 리스트 반환
@api_view(['POST'])
def get_teacher_list(request):
    try:
        data = list(Teacher.objects.filter(
            Q(name__icontains=request.data['search']) |
            Q(part__icontains=request.data['search']) |
            Q(resSubject__icontains=request.data['search'])
        ).values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)
    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)
