from django.urls import path
from students.views import home, add_student, student_list, update_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('add_student/', add_student, name='add_student'),
    path('student_list/', student_list, name='student_list'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student')
]