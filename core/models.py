from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    fcm_token = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    class_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='classrooms')
    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=50)  # e.g., "HK1 2022-2023"
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('teacher', 'subject', 'classroom', 'semester')
    
    def __str__(self):
        return f"{self.teacher} - {self.subject} - {self.classroom} - {self.semester}"

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"

class GradeType(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Điểm miệng", "Điểm 15p", "Điểm thi"
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    teacher_assignment = models.ForeignKey(TeacherAssignment, on_delete=models.CASCADE)
    grade_type = models.ForeignKey(GradeType, on_delete=models.CASCADE)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ('student', 'teacher_assignment', 'grade_type')
    
    def __str__(self):
        return f"{self.student} - {self.teacher_assignment.subject} - {self.grade_type} - {self.value}"

class GradeHistory(models.Model):
    ACTION_CHOICES = [
        ('update', 'Cập nhật'),
        ('delete', 'Xóa'),
        ('create', 'Tạo mới'),
    ]
    
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    old_value = models.FloatField(null=True, blank=True)
    new_value = models.FloatField(null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, default='update')
    
    def __str__(self):
        if self.action == 'delete':
            return f"{self.grade.student} - Điểm {self.old_value} bị xóa bởi {self.modified_by}"
        elif self.action == 'create':
            return f"{self.grade.student} - Điểm {self.new_value} được tạo bởi {self.modified_by}"
        else:
            return f"{self.grade.student} - Thay đổi từ {self.old_value} thành {self.new_value} bởi {self.modified_by}"
        
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
