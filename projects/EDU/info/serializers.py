from rest_framework import serializers
from . import models


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = \
            '__all__'


class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attend
        fields = \
            '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work
        fields = \
            '__all__'


class SuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Suggest
        fields = \
            '__all__'


class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consult
        fields = \
            '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Analysis
        fields = \
            '__all__'
