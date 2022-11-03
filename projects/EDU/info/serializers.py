from rest_framework import serializers
from . import models


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = \
            '__all__'
