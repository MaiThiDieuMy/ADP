from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Common URLs
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin URLs
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/teachers/', views.teacher_list, name='teacher_list'),
    path('dashboard/teachers/create/', views.teacher_create, name='teacher_create'),
    path('dashboard/teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('dashboard/teachers/<int:teacher_id>/toggle-status/', views.teacher_toggle_status, name='teacher_toggle_status'),
    path('dashboard/teachers/<int:teacher_id>/delete/', views.teacher_delete, name='teacher_delete'),
    path('dashboard/teachers/<int:teacher_id>/reset-password/', views.teacher_reset_password, name='teacher_reset_password'),
    path('dashboard/teachers/<int:teacher_id>/update/', views.teacher_update, name='update_teacher'),
    
    # Student URLs
    path('dashboard/students/', views.student_list, name='student_list'),
    path('dashboard/students/create/', views.student_create, name='student_create'),
    path('dashboard/students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('dashboard/students/<int:student_id>/edit/', views.student_edit, name='student_edit'),
    path('dashboard/students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    
    path('dashboard/subjects/', views.subject_list, name='subject_list'),
    path('dashboard/subjects/create/', views.subject_create, name='subject_create'),
    path('subject/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    
    path('dashboard/classrooms/', views.classroom_list, name='classroom_list'),
    path('dashboard/classrooms/create/', views.classroom_create, name='classroom_create'),
    path('dashboard/classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),
    path('dashboard/classrooms/<int:classroom_id>/import-students/', views.classroom_import_students, name='classroom_import_students'),
    path('dashboard/classrooms/<int:classroom_id>/add-student/', views.classroom_add_student, name='classroom_add_student'),
    path('classroom/delete/<int:classroom_id>/', views.classroom_delete, name='classroom_delete'),
    
    path('dashboard/semesters/', views.semester_list, name='semester_list'),
    path('dashboard/semesters/create/', views.semester_create, name='semester_create'),
    path('dashboard/semesters/<int:semester_id>/update/', views.semester_update, name='semester_update'),
    path('dashboard/semesters/<int:semester_id>/toggle-status/', views.semester_toggle_status, name='semester_toggle_status'),
    path('dashboard/semesters/<int:semester_id>/delete/', views.semester_delete, name='semester_delete'),
    
    path('dashboard/assignments/', views.teacher_assignment_list, name='teacher_assignment_list'),
    path('dashboard/assignments/create/', views.teacher_assignment_create, name='teacher_assignment_create'),
    path('teacher-assignments/', views.teacher_assignment_list, name='teacher_assignment_list'),
    path('teacher-assignments/create/', views.teacher_assignment_create, name='teacher_assignment_create'),
    path('teacher-assignments/delete/', views.teacher_assignment_delete, name='teacher_assignment_delete'),
    
    # Teacher URLs
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher/change-password/', views.teacher_change_password, name='teacher_change_password'),
    path('teacher/assignments/<int:assignment_id>/grades/', views.class_grades, name='class_grades'),
    path('teacher/assignments/<int:assignment_id>/students/', views.teacher_class_students, name='teacher_class_students'),
    path('update-grade/', views.update_grade, name='update_grade'),
    path('update-grades/', views.update_grades, name='update_grades'),
    path('delete-grade/', views.delete_grade, name='delete_grade'),
    path('teacher/grade-history/', views.grade_history, name='grade_history'),
    path('teacher/assignments/<int:assignment_id>/manage-grade-types/', views.manage_grade_types, name='manage_grade_types'),
    path('teacher/assignments/<int:assignment_id>/bulk-update/', views.bulk_update_grades, name='bulk_update_grades'),
    path('teacher/assignments/<int:assignment_id>/upload/', views.upload_grades, name='upload_grades'),
    path('teacher/assignments/<int:assignment_id>/download/', views.download_grades, name='download_grades'),
    
    # Student routes
    path('student/dashboard_students/', views.dashboard_students, name='dashboard_students'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/grades/', views.student_grades, name='student_grades'),
    path('student/change-password/', views.student_change_password, name='student_change_password'),
    path('notifications/mark-read/', views.mark_notifications_read, name='mark_notifications_read'),
    path('save-fcm-token/', views.save_fcm_token, name='save_fcm_token'),

]