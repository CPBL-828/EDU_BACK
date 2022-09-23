from django.contrib import admin
from .models import Question
from .models import Answer


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question)
admin.site.register(Answer)
