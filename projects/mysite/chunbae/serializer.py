from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.Serializer):
    class Meta:
        model = Teacher
        fields = ('teacherKey', 'name', 'id')
