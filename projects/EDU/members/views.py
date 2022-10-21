# serializer 및 drf 사용
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializer 불러오기
from django.core import serializers
from . import serializers
from .serializers import TeacherSerializer, AdminSerializer, StudentSerializer, ParentSerializer
# 모델 불러오기
from .models import Teacher, Admin, Student, Parent
# api_view 작성
from rest_framework.decorators import api_view
# JSON
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


# CUSTOM model 에 대한 view
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # 로그인 인증된 요청에 한해 view 호출 허용


member_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

member_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


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
                # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Admin.objects.get(id=data)
                # Teacher 모델 id=data인 데이터 조회
                info = Admin.objects.filter(id=data)
                # ident 값 serializer를 통해 json 파싱 / queryset => json
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
                # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Student.objects.get(id=data)
                # Teacher 모델 id=data인 데이터 조회
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
                # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
                ident = Parent.objects.get(id=data)
                # Teacher 모델 id=data인 데이터 조회
                info = Parent.objects.filter(id=data)
                # ident 값 serializer를 통해 json 파싱 / queryset => json
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
                return JsonResponse({'chunbae': '어서오세요, 주인님!'}, info_json.data, json_dumps_params={'ensure_ascii': False}, status=200)
            else:
                return JsonResponse({'message': '주인님이 아니시군요?'}, status=400)
        else:
            return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

    except KeyError:
        return JsonResponse({'chunbae': '잘못된 요청입니다.'}, status=400)

# querry = 'SELECT user_name FROM user_info '
# if(client.name){
# querry += 'WHEHE user_name = $' + client.name + ' ';
# }
#
#
# data = await db.cusor(querry, param);
