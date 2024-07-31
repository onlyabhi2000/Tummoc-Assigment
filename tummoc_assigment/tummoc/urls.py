from django.urls import path
from .views_student import StudentList, StudentDetail, HelloWorld
from .views_teacher import TeacherList, TeacherDetail
from .views_distance import DistanceView
from .views_auth import RegisterView, LoginView
urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('teachers/', TeacherList.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher_detail'),
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('distance/', DistanceView.as_view(), name='distance_calculation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
