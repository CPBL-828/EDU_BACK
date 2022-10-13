# serializer 및 drf 사용
from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework import permissions


# Teacher model 에 대한 view
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # 로그인 인증된 요청에 한해 view 호출 허용

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
