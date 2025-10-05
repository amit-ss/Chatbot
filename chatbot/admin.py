from django.contrib import admin

# Register your models here. 
from django.contrib import admin
from chatbot.models import Faculty, Course, ClassTimetable, ExamSchedule

admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(ClassTimetable)
admin.site.register(ExamSchedule)