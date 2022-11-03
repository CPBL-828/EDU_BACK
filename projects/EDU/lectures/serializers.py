from rest_framework import serializers
from . import models


class LectureRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LectureRoom
        fields = \
            '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecture
        fields = \
            '__all__'
