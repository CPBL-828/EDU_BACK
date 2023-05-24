import os
import shutil
# serializer 및 drf 사용
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializer 불러오기
from django.core import serializers as core_serializers
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
from django.db.models import F
# 시간 관련 기능
import datetime
# settings 불러오기
from config.settings import base


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


def get_profile_image(request, path):
    try:
        # 이미지 파일 경로
        file_path = os.path.join(base.MEDIA_ROOT, 'profile', path)
        print(file_path)
        # 파일이 존재하는지 확인
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                # 이미지 파일을 HttpResponse에 담아 리턴
                response = HttpResponse(f.read(), content_type="image/jpeg")
                return response
        else:
            return JsonResponse({'chunbae': '파일을 찾을 수 없습니다.'}, status=404)

    except FileNotFoundError:
        return JsonResponse({'chunbae': ' 파일을 찾을 수 없습니다.'}, status=404)


@api_view(['POST'])
def testLinkedData(request):
    student_data = Student.objects.all()
    parent_data = Parent.objects.all()

    combined_data = student_data.annotate(

    )

    result = {'student': student_data, 'parent': parent_data}

    return JsonResponse(result)


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
        if len(request.data["userKey"]) > 0 and len(request.data['lectureKey']) == 0:

            try:
                if Teacher.objects.filter(teacherKey=request.data["userKey"]).exists():
                    # 받은 userKey와 teacherKey와 매칭
                    key = Teacher.objects.get(teacherKey=request.data["userKey"])
                    # 강사키에 맞는 강의 리스트 정렬 : 중복 강의명 제거)
                    lecture = Lecture.objects.filter(teacherKey=key).values('lectureKey').distinct('lectureName')
                    # 강의키에 맞는 학생 리스트 정렬
                    student = LectureStatus.objects.filter(lectureKey__in=lecture).values('studentKey')
                    # 학생 리스트 생성 : 검색 기능 포함
                    data = list(Student.objects.filter(studentKey__in=student).filter(
                        Q(name__icontains=request.data['search']) |
                        Q(school__icontains=request.data['search']) |
                        Q(grade__icontains=request.data['search'])
                    ).order_by('name').values())

                    result = {'resultData': data, 'count': len(data)}

                    return JsonResponse(result, status=200)

                else:
                    data = list(Student.objects.filter(
                        Q(name__icontains=request.data['search']) |
                        Q(school__icontains=request.data['search']) |
                        Q(grade__icontains=request.data['search'])
                    ).order_by('name').values())

                    result = {'resultData': data, 'count': len(data)}

                    return JsonResponse(result, status=200)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data["userKey"]) > 0 and len(request.data['lectureKey']) > 0:

            try:
                if Teacher.objects.filter(teacherKey=request.data["userKey"]).exists():
                    # 받은 userKey와 teacherKey와 매칭
                    key = Teacher.objects.get(teacherKey=request.data["userKey"])
                    student = LectureStatus.objects.filter(lectureKey=request.data['lectureKey']).values('studentKey')

                    data = list(Student.objects.filter(studentKey__in=student).filter(
                        Q(name__icontains=request.data['search']) |
                        Q(school__icontains=request.data['search']) |
                        Q(grade__icontains=request.data['search'])
                    ).order_by('name').values())

                    result = {'resultData': data, 'count': len(data)}
                    return JsonResponse(result, status=200)

                else:
                    return JsonResponse({'chunbae': 'key 확인 바랍니다.'}, status=400)

            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data["userKey"]) == 0 and len(request.data['lectureKey']) > 0:
            try:
                student = LectureStatus.objects.filter(lectureKey=request.data['lectureKey']).values('studentKey')

                data = list(Student.objects.filter(studentKey__in=student).filter(
                    Q(name__icontains=request.data['search']) |
                    Q(school__icontains=request.data['search']) |
                    Q(grade__icontains=request.data['search'])
                ).order_by('name').values())

                result = {'resultData': data, 'count': len(data)}
                return JsonResponse(result, status=200)
            except KeyError:
                return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

        elif len(request.data["userKey"]) == 0 and len(request.data['lectureKey']) == 0:

            data = list(Student.objects.filter(
                Q(name__icontains=request.data['search']) |
                Q(school__icontains=request.data['search']) |
                Q(grade__icontains=request.data['search'])
            ).order_by('name').values())

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

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_student(request):
    try:
        if Student.objects.filter(studentKey=request.data['studentKey']).exists():

            student = Student.objects.get(studentKey=request.data['studentKey'])

            serializer = StudentSerializer(student, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                Student.objects.filter(studentKey=request.data['studentKey']).update(editDate=datetime.datetime.now())

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
def edit_student_profile(request):
    try:
        if Student.objects.filter(studentKey=request.data['studentKey']).exists():

            student = Student.objects.get(studentKey=request.data['studentKey'])
            profile_pic = request.FILES.get('profileImg', None)
            old_profile_img = student.profileImg

            serializer = StudentSerializer(student, data=request.data, partial=True)

            if serializer.is_valid():
                # 프로필 이미지 처리
                if profile_pic:
                    # 기존 이미지 파일 삭제
                    if old_profile_img:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_profile_img.name)
                        os.remove(old_file_path)

                    file_extension = profile_pic.name.split('.')[-1]
                    file_name = f"profile/{student}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(profile_pic.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, profile_pic.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT,  file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.profileImg.name = os.path.join(file_name)
                    serializer.instance.save(update_fields=['profileImg'])
                else:  # 프로필 이미지를 삭제하는 경우
                    # 기존 이미지 파일 삭제
                    if old_profile_img:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_profile_img.name)
                        os.remove(old_file_path)
                    serializer.instance.profileImg = None
                    serializer.instance.save(update_fields=['profileImg'])

                Student.objects.filter(studentKey=request.data['studentKey']).update(editDate=datetime.datetime.now())

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
def delete_student(request):
    try:
        if Student.objects.filter(studentKey=request.data['studentKey']).exists():

            student = Student.objects.filter(studentKey=request.data['studentKey'])
            student.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

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
        ).order_by('name').values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)
    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_teacher_detail(request):
    try:
        data = list(Teacher.objects.filter(
            teacherKey=request.data['teacherKey']
        ).values())

        result = {'resultData': data}

        return JsonResponse(result, status=200)
    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_teacher(request):
    try:
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            # 파일 이름 설정
            serializer.save()

            result = {'chunbae': '데이터 생성.', 'resultData': serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'chunbae': '생성 오류.', 'resultData': serializer.errors}
            return JsonResponse(result, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def edit_teacher(request):
    try:
        if Teacher.objects.filter(teacherKey=request.data['teacherKey']).exists():

            teacher = Teacher.objects.get(teacherKey=request.data['teacherKey'])

            serializer = TeacherSerializer(teacher, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                Teacher.objects.filter(teacherKey=request.data['teacherKey']).update(editDate=datetime.datetime.now())

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
def edit_teacher_profile(request):
    try:
        if Teacher.objects.filter(teacherKey=request.data['teacherKey']).exists():

            teacher = Teacher.objects.get(teacherKey=request.data['teacherKey'])
            profile_pic = request.FILES.get('profileImg')
            old_profile_img = teacher.profileImg

            serializer = TeacherSerializer(teacher, data=request.data, partial=True)

            if serializer.is_valid():
                # 프로필 이미지 처리
                if profile_pic:
                    # 기존 이미지 파일 삭제
                    if old_profile_img:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_profile_img.name)
                        os.remove(old_file_path)

                    file_extension = profile_pic.name.split('.')[-1]
                    file_name = f"{teacher}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, 'profile', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(profile_pic.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, 'profile', profile_pic.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT, 'profile', file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.profileImg.name = os.path.join('profile', file_name)
                    serializer.instance.save(update_fields=['profileImg'])
                else:  # 프로필 이미지를 삭제하는 경우
                    # 기존 이미지 파일 삭제
                    if old_profile_img:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_profile_img.name)
                        os.remove(old_file_path)
                    serializer.instance.profileImg = None
                    serializer.instance.save(update_fields=['profileImg'])

                Teacher.objects.filter(teacherKey=request.data['teacherKey']).update(editDate=datetime.datetime.now())

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
def edit_teacher_resume(request):
    try:
        if Teacher.objects.filter(teacherKey=request.data['teacherKey']).exists():

            teacher = Teacher.objects.get(teacherKey=request.data['teacherKey'])
            resume = request.FILES.get('resume')
            old_resume = teacher.resume

            serializer = TeacherSerializer(teacher, data=request.data, partial=True)

            if serializer.is_valid():
                # 이력서 파일 처리
                if resume:
                    # 기존 이력서 파일 삭제
                    if old_resume:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_resume.name)
                        os.remove(old_file_path)

                    file_extension = resume.name.split('.')[-1]
                    file_name = f"{teacher}.{file_extension}"
                    file_path = os.path.join(base.MEDIA_ROOT, 'resume', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(resume.read())
                    # 이미 저장된 파일의 이름 변경
                    old_file_path = os.path.join(base.MEDIA_ROOT, 'resume', resume.name)
                    new_file_path = os.path.join(base.MEDIA_ROOT, 'resume', file_name)
                    if os.path.exists(old_file_path):
                        shutil.move(old_file_path, new_file_path)
                    serializer.instance.resume.name = os.path.join('resume', file_name)
                    serializer.instance.save(update_fields=['resume'])
                else:  # 이력서 파일을 삭제하는 경우
                    # 이력서 파일 삭제
                    if old_resume:
                        old_file_path = os.path.join(base.MEDIA_ROOT, old_resume.name)
                        os.remove(old_file_path)
                    serializer.instance.resume = None
                    serializer.instance.save(update_fields=['resume'])

                Teacher.objects.filter(teacherKey=request.data['teacherKey']).update(editDate=datetime.datetime.now())

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
def delete_teacher(request):
    try:
        if Teacher.objects.filter(teacherKey=request.data['teacherKey']).exists():

            teacher = Teacher.objects.filter(teacherKey=request.data['teacherKey'])
            teacher.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def get_parent_list(request):
    try:
        data = list(Parent.objects.filter(
            Q(name__icontains=request.data['search'])
        ).order_by('name').values())

        result = {'resultData': data, 'count': len(data)}

        return JsonResponse(result, status=200)
    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)


@api_view(['POST'])
def create_parent(request):
    try:
        serializer = ParentSerializer(data=request.data)
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
def edit_parent(request):
    try:
        if Parent.objects.filter(parentKey=request.data['parentKey']).exists():

            parent = Parent.objects.get(parentKey=request.data['parentKey'])

            serializer = ParentSerializer(parent, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                Parent.objects.filter(parentKey=request.data['parentKey']).update(editDate=datetime.datetime.now())

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
def delete_parent(request):
    try:
        if Parent.objects.filter(parentKey=request.data['parentKey']).exists():

            parent = Parent.objects.filter(parentKey=request.data['parentKey'])
            parent.delete()

            return JsonResponse({'chunbae': '데이터 삭제.'}, status=200)
        else:
            return JsonResponse({'chunbae': '삭제되지 않았습니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)
