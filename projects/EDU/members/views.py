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


# CUSTOM model 에 대한 view
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    # 로그인 인증된 요청에 한해 view 호출 허용

    @action(detail=False, methods=['post'])
    def compare(self, request):
        data = request.data['id']
        ident = Teacher.objects.filter(id=data).values()

        print("request >> ", data)
        print("ident : ", ident)

        return HttpResponse(ident)
        # if ident['id'] == data:
        #     return HttpResponse('Yeah')
        # else:
        #     return HttpResponse('wrong')


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
