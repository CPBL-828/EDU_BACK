# serializer 및 drf 사용
import json
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TeacherSerializer
from .models import Teacher
# JSON
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core import serializers


# CUSTOM model 에 대한 view
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_teacher = TeacherSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    # 로그인 인증된 요청에 한해 view 호출 허용

    # Teacher id & 수신 데이터 비교
    @action(detail=False, methods=['post'])
    def compare(self, request):

        # 수신 데이터 data에 저장
        data = request.data['id']

        # Teacher 모델에서 수신 데이터와 매치되는 값 ident에 저장
        ident = Teacher.objects.get(id=data)
        info = Teacher.objects.filter(id=data)
        info_json = TeacherSerializer(ident)

        print('ident >>> : ', ident.id)
        print('주노주노 >>> ', info_json)
        print('info_json.data >>> : \n', info_json.data)

        try:
            if info.exists():
                # ident는 키를 반환, 해당 키를 가진 모델의 id 필드값과 data 비교
                if ident.id == data:
                    return JsonResponse(info_json.data, json_dumps_params={'ensure_ascii': False},  status=200)
                else:
                    return JsonResponse({'message': 'sinba~'}, status=400)
            else:
                return HttpResponse(status=400)

        except KeyError:
            return HttpResponse(status=400)


teacher_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

teacher_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
