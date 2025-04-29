from django.contrib import admin
from .models import (
    Teacher, Subject, ClassRoom, Semester, 
    TeacherAssignment, Student, GradeType, Grade, GradeHistory
)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('class_code', 'name')
    search_fields = ('class_code', 'name')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(TeacherAssignment)
class TeacherAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject', 'classroom', 'semester')
    list_filter = ('subject', 'classroom', 'semester')
    search_fields = ('teacher__user__username', 'subject__name', 'classroom__name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'get_classrooms')
    list_filter = ('classrooms',)
    search_fields = ('student_id', 'name')

    def get_classrooms(self, obj):
            return ", ".join([classroom.name for classroom in obj.classrooms.all()])
    get_classrooms.short_description = 'Lớp học'

@admin.register(GradeType)
class GradeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher_assignment', 'grade_type', 'value', 'updated_at')
    list_filter = ('grade_type', 'teacher_assignment__subject', 'teacher_assignment__classroom')
    search_fields = ('student__name', 'student__student_id')

@admin.register(GradeHistory)
class GradeHistoryAdmin(admin.ModelAdmin):
    list_display = ('grade', 'old_value', 'new_value', 'modified_by', 'modified_at')
    list_filter = ('modified_at',)
    search_fields = ('grade__student__name', 'modified_by__username')
