from django.db import models

 

# --- Faculty Contacts Model ---
class Faculty(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

# --- Course/Subject Model (for Timetable and Exams) ---
class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10, unique=True)
    assigned_faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

# --- Class Timetable Model ---
class ClassTimetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    DAY_CHOICES = [
        ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), 
        ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')
    ]
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=50)

    class Meta:
        ordering = ['day_of_week', 'start_time']
        verbose_name_plural = "Class Timetable"

    def __str__(self):
        return f"{self.course.code} - {self.day_of_week} ({self.start_time}-{self.end_time})"

# --- Exam Schedule Model ---
class ExamSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=50)

    class Meta:
        ordering = ['exam_date', 'start_time']

    def __str__(self):
        return f"Exam: {self.course.code} on {self.exam_date}"

# chatbot/models.py

from django.db import models

class ChatMessage(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('ai', 'AI Assistant'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, db_index=True) # Tracks the conversation

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.role.upper()} ({self.session_id}): {self.content[:50]}"