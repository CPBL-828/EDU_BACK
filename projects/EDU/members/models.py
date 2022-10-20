from django.db import models


# 강사 모델 생성
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


# 관리자 모델 생성
class Admin(models.Model):
    adminKey = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=10)
    id = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.adminKey


# class Student(models.Model):
#     studentKey = models.CharField(max_length=50, primary_key=True)
#     name = models.CharField(max_length=50)
#     birth = models.DateField()
#     sex = models.CharField(max_length=1)
#     phone = models.CharField(max_length=11)
#     school = models.CharField(max_length=10)
#     grade = models.CharField(max_length=10)
#     address = models.CharField(max_length=50)
#     remark = models.TextField()
#     delState = models.CharField(max_length=1)
#     profileImg = models.CharField(max_length=50)
#     createDate = models.DateTimeField(auto_now_add=True)
#     editDate = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.studentKey

# class parent(models.Model):
#     parentKey = models.CharField(max_length=50, primary_key=True)
#