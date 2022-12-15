from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.student_register),
    # path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('user-login',views.student_login),
    path('matchs',views.getMatchs)
]
