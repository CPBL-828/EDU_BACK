# serializer 및 drf 사용
import json
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . import serializers
from .serializers import TeacherSerializer, AdminSerializer
from .models import Teacher, Admin
# api_view 작성
from rest_framework.decorators import api_view
# JSON
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core import serializers


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

        # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
        ident = Teacher.objects.get(id=data)
        # Teacher 모델 id=data인 데이터 조회
        info = Teacher.objects.filter(id=data)
        # ident 값 serializer를 통해 json 파싱 / queryset => json
        info_json = TeacherSerializer(ident)

    elif user_type == 'ADM':

        queryset = Admin.objects.all()
        serializer_class = AdminSerializer

        ident = Admin.objects.get(id=data)
        info = Admin.objects.filter(id=data)
        info_json = AdminSerializer(ident)

    # elif user_type == 'STU':
    #
    # elif user_type == 'PAR':

    try:
        if info.exists():
            # ident는 키를 반환, 해당 키를 가진 모델의 id 필드값과 data 비교
            if ident.id == data:
                # {'ensure_ascii' : False} => json 문자열이 한글로 표시되도록
                return JsonResponse(info_json.data, json_dumps_params={'ensure_ascii': False}, status=200)
            else:
                return JsonResponse({'message': 'sinba~'}, status=400)
        else:
            return HttpResponse(status=400)

    except KeyError:
        return HttpResponse(status=400)
