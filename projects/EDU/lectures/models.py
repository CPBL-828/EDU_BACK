from django.db import models
import os
# 랜덤 문자열 생성
import uuid
import shortuuid
from shortuuid.django_fields import ShortUUIDField
# 모델 import
from members.models import *


# 강의 관련 모델 작성

# 강의실 모델 작성
class LectureRoom(models.Model):
    roomKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                               verbose_name='강의실키')
    name = models.CharField(max_length=10, unique=True, verbose_name='강의실명')
    type = models.CharField(max_length=10, verbose_name='유형')
    totalPeople = models.IntegerField(verbose_name='총수용인원')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.roomKey


# 강의 모델 작성
class Lecture(models.Model):
    lectureKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='강의키')
    roomKey = models.ForeignKey('LectureRoom', on_delete=models.CASCADE, db_column='roomKey', verbose_name='강의실키')
    teacherKey = models.ForeignKey('members.Teacher', on_delete=models.CASCADE, db_column='teacherKey',
                                   verbose_name='강사키')
    adminKey = models.CharField(max_length=50, blank=True, null=True, db_column='adminKey', verbose_name='관리자키')
    lectureName = models.CharField(max_length=10, verbose_name='강의명')
    roomName = models.CharField(max_length=10, verbose_name='강의실명')
    teacherName = models.CharField(max_length=10, verbose_name='강사명')
    type = models.CharField(max_length=10, verbose_name='강의유형')
    subject = models.CharField(max_length=10, verbose_name='과목')
    color = models.CharField(max_length=10, blank=True, null=True, verbose_name='과목색상')
    book = models.CharField(max_length=50, verbose_name='주교재')
    target = models.CharField(max_length=10, verbose_name='대상학년')
    day = models.IntegerField(verbose_name='요일')
    startTime = models.CharField(max_length=5, verbose_name='시작시간')
    duration = models.IntegerField(verbose_name='지속시간')
    startDate = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='등록일자')
    endDate = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='마감일자')
    progress = models.CharField(default='등록 대기 중', max_length=10, verbose_name='진행상태')
    reason = models.TextField(blank=True, verbose_name='사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.lectureKey


# 수강 현황 테이블 생성
class LectureStatus(models.Model):
    lectureStatusKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True,
                                        editable=False,
                                        verbose_name='수강현황키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    lectureKey = models.ForeignKey('Lecture', on_delete=models.CASCADE, db_column='lectureKey', verbose_name='강의키')
    state = models.CharField(max_length=10, blank=True, verbose_name='수강상태')
    reason = models.TextField(blank=True, verbose_name='사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')


# 과제 테이블 생성
class Assign(models.Model):
    assignKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True,
                                 editable=False,
                                 verbose_name='과제키')
    lectureKey = models.ForeignKey('Lecture', on_delete=models.CASCADE, db_column='lectureKey', verbose_name='강의키')
    lectureName = models.CharField(max_length=10, verbose_name='강의명')
    # studentKey = models.CharField(max_length=50, blank=True, null=True, verbose_name='학생키')
    # studentName = models.CharField(max_length=10, blank=True, null=True, verbose_name='학생명')
    assignment = models.CharField(max_length=50, verbose_name='과제첨부')
    content = models.TextField(verbose_name='과제내용')
    deadLine = models.DateTimeField(verbose_name="마감일자")
    # status = models.CharField(max_length=10, verbose_name='제출상태')
    # score = models.FloatField(verbose_name='점수')
    type = models.CharField(max_length=10, verbose_name='과제유형')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')


class AssignStatus(models.Model):
    assignStatusKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True,
                                       editable=False,
                                       verbose_name='과제현황키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    studentName = models.CharField(max_length=10, verbose_name='학생명')
    assignKey = models.ForeignKey('Assign', on_delete=models.CASCADE, db_column='assignKey', verbose_name='과제키')
    assignState = models.CharField(max_length=10, default='미제출', verbose_name='제출상태')
    assignScore = models.FloatField(blank=True, null=True, verbose_name='점수')
    assignNote = models.TextField(blank=True, verbose_name='비고')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')


# 시험 테이블 생성
class Test(models.Model):
    testKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                               verbose_name='시험키')
    lectureKey = models.ForeignKey('Lecture', on_delete=models.CASCADE, db_column='lectureKey', verbose_name='강의키')
    lectureName = models.CharField(max_length=10, verbose_name='강의명')
    testDate = models.DateTimeField(verbose_name='시험일자')
    testType = models.CharField(max_length=10, verbose_name='시험유형')
    testSheet = models.CharField(null=True, blank=True, max_length=50, verbose_name='시험지링크')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.testKey


# 시험 현황 테이블 생성
class TestStatus(models.Model):
    testStatusKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                     verbose_name='시험현황키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    studentName = models.CharField(max_length=10, verbose_name='학생명')
    testKey = models.ForeignKey('Test', on_delete=models.CASCADE, db_column='testKey', verbose_name='시험키')
    state = models.CharField(max_length=1, default='N', verbose_name='응시여부')
    reason = models.TextField(blank=True, verbose_name='사유')
    testProgress = models.CharField(max_length=10, default='예정', verbose_name='진행상태')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.testStatusKey


# 성적 테이블 생성
class Record(models.Model):
    recordKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                 verbose_name='성적키')
    testStatusKey = models.ForeignKey('TestStatus', on_delete=models.CASCADE, db_column='testStatusKey',
                                      verbose_name='시험현황키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    recordAnalysis = models.TextField(verbose_name='성적분석')
    score = models.FloatField(verbose_name='점수')
    rating = models.CharField(max_length=1, verbose_name='등급')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.recordKey


# 강의 계획서 생성
class Planner(models.Model):
    plannerKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='계획서키')
    lectureKey = models.ForeignKey('Lecture', on_delete=models.CASCADE, db_column='lectureKey', verbose_name='강의키')
    lectureName = models.CharField(max_length=10, verbose_name='강의명')
    teacherKey = models.ForeignKey('members.Teacher', on_delete=models.CASCADE, db_column='teacherKey',
                                   verbose_name='강사키')
    teacherName = models.CharField(max_length=10, verbose_name='강사명')
    day = models.DateTimeField(verbose_name='강의일자')
    content = models.TextField(verbose_name='내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.plannerKey
