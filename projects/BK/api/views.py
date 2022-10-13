from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework import permissions


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
