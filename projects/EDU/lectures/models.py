from django.db import models
from ..members.models import Teacher, Admin


# 강의 관련 모델 작성

# 강의실 모델 작성
class LectureRoom(models.Model):
    roomKey = models.CharField(max_length=50, verbose_name='강의실키')
    name = models.CharField(max_length=10, verbose_name='강의실명')
    type = models.CharField(max_length=10, verbose_name='유형')
    totalPeople = models.IntegerField(verbose_name='총수용인원')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(auto_now=True, verbose_name='수정일')


# 강의 모델 작성
class Lecture(models.Model):
    lectureKey = models.CharField(max_length=50)
    roomKey = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    adminKey = models.ForeignKey('Admin', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

