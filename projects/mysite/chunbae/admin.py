from django.contrib import admin
from .models import Teacher


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Teacher)
