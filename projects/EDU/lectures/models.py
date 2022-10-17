from django.db import models
from ..members.models import Teacher, Admin


# 강의실 모델 작성
# class LectureRoom(models.Model):
#     roomKey = models.CharField(max_length=50)
#     name = models.CharField(max_length=10)
#     type = models.CharField(max_length=10)
#     totalPeople = models.IntegerField
#     createDate = models.DateTimeField(auto_now_add=True)
#     editDate = models.DateTimeField(auto_now=True)


# 강의 모델 작성
# class Lecture(models.Model):
#     lectureKey = models.CharField(max_length=50)
#     roomKey = models.ForeignKey('Teacher', on_delete=models.CASCADE)
#     adminKey = models.ForeignKey('Admin', on_delete=models.CASCADE)
#     name = models.CharField(max_length=10)
#     type = models.CharField(max_length=10)
