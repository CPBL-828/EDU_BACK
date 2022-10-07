from django.db import models


# 강사 model 생성
class Teacher(models.Model):
    teacherKey = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=50)
    part = models.CharField(max_length=10)
    resSubject = models.CharField(max_length=10)
    joinDate = models.DateTimeField(auto_now_add=True)
    leaveDate = models.DateTimeField(auto_now=True)
    resume = models.CharField(max_length=50)
    profileImg = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacherKey
