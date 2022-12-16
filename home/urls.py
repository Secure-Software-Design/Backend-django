from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_register),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('user-login',views.user_login),
    path('matchs',views.getMatchs)
]
