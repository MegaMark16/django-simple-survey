from django.contrib import admin

from models import Survey, Question, Response, Answer

class QuestionInline(admin.TabularInline):
    model = Question

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ['name', ]
    inlines = [
        QuestionInline,
    ]

class AnswerInline(admin.TabularInline):
    model = Answer
    readonly_fields = ['answer', 'question']
    extra = 0

class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey', ]
    list_filter = ['survey',]
    readonly_fields = ['survey',]
    inlines = [
        AnswerInline,
    ]
    
admin.site.register(Response, ResponseAdmin)    
admin.site.register(Survey, SurveyAdmin)


