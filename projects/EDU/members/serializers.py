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


class StudentSerializer(serializers.ModelSerializer):
    profileImg = serializers.ImageField()
    class Meta:
        model = models.Student
        fields = \
            '__all__'


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parent
        fields = \
            '__all__'
