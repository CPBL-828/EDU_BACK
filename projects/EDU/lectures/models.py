import os
from django.db import models
from members.models import *


# 강의 관련 모델 작성

# 강의실 모델 작성
class LectureRoom(models.Model):
    roomKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False, verbose_name='강의실키')
    name = models.CharField(max_length=10, verbose_name='강의실명')
    type = models.CharField(max_length=10, verbose_name='유형')
    totalPeople = models.IntegerField(verbose_name='총수용인원')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.roomKey


# 강의 모델 작성
class Lecture(models.Model):
    lectureKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False, verbose_name='강의키')
    roomKey = models.ForeignKey('LectureRoom', on_delete=models.CASCADE, verbose_name='강의실키')
    teacherKey = models.ForeignKey('members.Teacher', on_delete=models.CASCADE, verbose_name='강사키')
    adminKey = models.ForeignKey('members.Admin', on_delete=models.CASCADE, verbose_name='관리자키')
    name = models.CharField(max_length=10, verbose_name='강의명')
    type = models.CharField(max_length=10, verbose_name='강의유형')
    subject = models.CharField(max_length=10, verbose_name='과목')
    book = models.CharField(max_length=50, verbose_name='주교재')
    target = models.CharField(max_length=10, verbose_name='대상학년')
    day = models.CharField(max_length=1, verbose_name='요일')
    startTime = models.CharField(max_length=5, verbose_name='시작시간')
    duration = models.IntegerField(verbose_name='지속시간')
    suggestDate = models.DateTimeField(auto_now=True, verbose_name='건의일자')
    progress = models.CharField(max_length=10, verbose_name='진행상태')
    reason = models.TextField(blank=True, verbose_name='사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.lectureKey
