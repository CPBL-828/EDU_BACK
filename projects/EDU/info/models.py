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
    readerKey = models.CharField(max_length=50, null=True, blank=True, verbose_name='열람대상')
    readerName = models.CharField(max_length=10, blank=False, null=True, verbose_name='열람대상자명')
    delState = models.CharField(max_length=1, default='N', verbose_name='삭제상태')
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
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    studentName = models.CharField(max_length=10, verbose_name='학생명')
    lectureKey = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE, db_column='lectureKey',
                                   verbose_name='강의키')
    lectureName = models.CharField(max_length=10, verbose_name='강의명')
    state = models.CharField(max_length=10, verbose_name='출석여부')
    reason = models.TextField(blank=True, verbose_name='수정사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.attendKey


# 근무 테이블 생성
class Work(models.Model):
    workKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                               verbose_name='근무키')
    teacherKey = models.ForeignKey('members.Teacher', on_delete=models.CASCADE, db_column='teacherKey',
                                   verbose_name='강사키')
    state = models.CharField(max_length=10, verbose_name='상태')
    reason = models.TextField(blank=True, verbose_name='사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.workKey


# 건의 테이블 생성
class Suggest(models.Model):
    suggestKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='건의키')
    adminKey = models.CharField(max_length=50, blank=True, null=True, db_column='adminKey', verbose_name='관리자키')
    writerKey = models.CharField(max_length=50, verbose_name='작성자')
    writerName = models.CharField(max_length=10, verbose_name='작성자이름')
    writerType = models.CharField(max_length=10, verbose_name='작성자유형')
    type = models.CharField(max_length=10, verbose_name='건의유형')
    state = models.CharField(max_length=1, default='N', verbose_name='처리여부')
    content = models.TextField(verbose_name='건의내용')
    answer = models.TextField(blank=True, verbose_name='답변내용')
    answerDate = models.DateTimeField(null=True, blank=True, verbose_name='답변날짜')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.suggestKey


# 상담 테이블 생성
class Consult(models.Model):
    consultKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                  verbose_name='상담키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    studentName = models.CharField(max_length=10, verbose_name='학생명')
    targetKey = models.CharField(max_length=50, verbose_name='상담담당')
    targetName = models.CharField(max_length=10, verbose_name='담당이름')
    consultDate = models.DateTimeField(verbose_name='상담날짜')
    consultType = models.CharField(max_length=10, verbose_name='상담유형')
    content = models.TextField(blank=True, verbose_name='상담내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.consultKey


# 분석 테이블 생성
class Analysis(models.Model):
    analysisKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                   verbose_name='분석키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    studentName = models.CharField(max_length=10, verbose_name='학생명')
    writerKey = models.CharField(max_length=50, verbose_name='작성자')
    writerName = models.CharField(max_length=10, verbose_name='작성자이름')
    content = models.TextField(verbose_name='분석내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.analysisKey


class Presence(models.Model):
    presenceKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False,
                                   verbose_name='전체출석키')
    studentKey = models.ForeignKey('members.Student', on_delete=models.CASCADE, db_column='studentKey',
                                   verbose_name='학생키')
    state = models.CharField(default='결석', max_length=10, verbose_name='출석여부')
    reason = models.TextField(blank=True, verbose_name='수정사유')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    editDate = models.DateTimeField(null=True, blank=True, verbose_name='수정일')
