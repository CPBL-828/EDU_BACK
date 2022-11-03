from django.db import models
from members.models import *


class Notice(models.Model):
    noticeKey = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, unique=True, editable=False, verbose_name='학생키')
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


