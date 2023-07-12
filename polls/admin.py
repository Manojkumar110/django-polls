from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


# class ChoiceModelAdmin(admin.StackedInline):
#     model = Choice
#     extra = 2


class ChoiceModelAdmin(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionModelAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    list_display = ['pub_date', 'question_text',]
    list_filter = ['pub_date']
    inlines = [ChoiceModelAdmin]

admin.site.register(Question, QuestionModelAdmin),
# admin.site.register(Choice)