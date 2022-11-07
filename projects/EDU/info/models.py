from django.db import models
# 랜덤 문자열 생성
import uuid
import shortuuid
from shortuuid.django_fields import ShortUUIDField
# 모델 import
from members.models import *
from lectures.models import *


# 공지 테이블 생성
class Notice(models.Model):
    noticeKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                 verbose_name='공지키')
    type = models.CharField(max_length=10, verbose_name='유형')
    writerKey = models.CharField(max_length=50, verbose_name='작성자')
    readerKey = models.CharField(max_length=50, blank=True, verbose_name='열람대상')
    delState = models.CharField(max_length=1, verbose_name='삭제상태')
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.noticeKey


# 출석 테이블 생성
class Attend(models.Model):
    attendKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                 verbose_name='출석키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, verbose_name='학생키')
    lectureKey = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE, verbose_name='강의키')
    state = models.CharField(max_length=10, verbose_name='출석여부')
    reason = models.TextField(verbose_name='수정사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.attendKey


# 근무 테이블 생성
class Work(models.Model):
    workKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                               verbose_name='근무키')
    teacherKey = models.ForeignKey('members.Teacher', on_delete=models.CASCADE, verbose_name='강사키')
    state = models.CharField(max_length=10, verbose_name='상태')
    reason = models.TextField(verbose_name='사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.workKey


# 건의 테이블 생성
class Suggest(models.Model):
    suggestKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='건의키')
    adminKey = models.ForeignKey('members.Admin', null=True,  on_delete=models.CASCADE, verbose_name='관리자키')
    writerKey = models.CharField(max_length=50, verbose_name='작성자')
    type = models.CharField(max_length=10, verbose_name='건의유형')
    state = models.CharField(max_length=10, verbose_name='처리여부')
    content = models.TextField(verbose_name='건의내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')


# 상담 테이블 생성
class Consult(models.Model):
    consultKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='상담키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, verbose_name='학생키')
    targetKey = models.CharField(max_length=50, verbose_name='상담담당')
    consultDate = models.DateTimeField(verbose_name='상담날짜')
    consultType = models.CharField(max_length=10, verbose_name='상담유형')
    content = models.TextField(verbose_name='상담내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')


# 분석 테이블 생성
class Analysis(models.Model):
    analysisKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                   verbose_name='분석키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, verbose_name='학생키')
    targetKey = models.CharField(max_length=50, verbose_name='작성자')
    content = models.TextField(verbose_name='분석내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')
