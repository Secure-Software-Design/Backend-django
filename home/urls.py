from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_register),
    # path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('student-login',views.student_login)
    # path('create-area',views.student_login)
]
