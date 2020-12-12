from django.contrib import admin
from .models import Question



# ---------------------------------------- 질문검색 ---------------------------------------- #
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
# ---------------------------------------- 질문검색 ---------------------------------------- #