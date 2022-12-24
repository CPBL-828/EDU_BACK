import os
# 랜덤 문자열 생성
import uuid
import shortuuid
from shortuuid.django_fields import ShortUUIDField
from django.db import models
from lectures.models import *


# 강사 모델 생성
class Teacher(models.Model):
    teacherKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='강사키')
    name = models.CharField(max_length=10, verbose_name='강사명')
    id = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name='강사id')

    def save(self, *args, **kwargs):
        if self.id is None:
            self.id = self.name + '-' + str(shortuuid.ShortUUID(alphabet="0123456789").random(length=4))

            super(Teacher, self).save(*args, **kwargs)

        else:
            self.id = self.id
            super(Teacher, self).save(*args, **kwargs)

    phone = models.CharField(max_length=11, verbose_name='연락처')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    link = models.CharField(max_length=50, verbose_name='개인링크')
    part = models.CharField(max_length=10, verbose_name='담당')
    resSubject = models.CharField(max_length=10, verbose_name='담당과목')
    joinDate = models.DateField(null=True, verbose_name='입사일')
    leaveDate = models.DateField(null=True, verbose_name='퇴사일')
    resume = models.CharField(max_length=50, verbose_name='이력서링크')
    profileImg = models.CharField(max_length=50, null=True, blank=True, verbose_name='프로필사진링크')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.teacherKey


# 관리자 모델 생성
class Admin(models.Model):
    adminKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                verbose_name='관리자')
    type = models.CharField(max_length=10, verbose_name='관리자유형')
    id = ShortUUIDField(length=6, max_length=6, unique=True, editable=False, verbose_name='관리자id')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.adminKey


# 학생 모델 생성
class Student(models.Model):
    studentKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='학생키')
    parentKey = models.ForeignKey('Parent', on_delete=models.CASCADE, db_column='parentKey', verbose_name='부모키')
    name = models.CharField(max_length=10, verbose_name='학생명')
    id = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name='학생id')

    def save(self, *args, **kwargs):

        if self.id is None:
            self.id = self.name + '-' + str(shortuuid.ShortUUID(alphabet="0123456789").random(length=4))
            super(Student, self).save(*args, **kwargs)

        else:
            self.id = self.id
            super(Student, self).save(*args, **kwargs)

    birth = models.DateField(verbose_name='생년월일')
    sex = models.CharField(max_length=1, verbose_name='성별')
    phone = models.CharField(max_length=11, verbose_name='연락처')
    emergency = models.CharField(max_length=11, verbose_name='비상연락망')
    school = models.CharField(max_length=10, verbose_name='학교명')
    grade = models.CharField(max_length=10, verbose_name='학년')
    address = models.CharField(max_length=50, verbose_name='주소')
    remark = models.TextField(blank=True, verbose_name='특이사항')
    delState = models.CharField(max_length=1, default='N', verbose_name='삭제여부')
    profileImg = models.CharField(max_length=50, null=True, blank=True, verbose_name='프로필사진링크')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.studentKey


# 학부모 모델 생성
class Parent(models.Model):
    parentKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                 verbose_name='부모키')
    name = models.CharField(max_length=10, verbose_name='이름')
    id = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='부모id')

    def save(self, *args, **kwargs):
        if self.id is None:

            self.id = self.name + '-' + str(shortuuid.ShortUUID(alphabet="0123456789").random(length=4))
            super(Parent, self).save(*args, **kwargs)

        else:
            self.id = self.id
            super(Parent, self).save(*args, **kwargs)

    phone = models.CharField(max_length=11, verbose_name='연락처')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.parentKey
