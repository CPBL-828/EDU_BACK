from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = \
            '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = \
            '__all__'
