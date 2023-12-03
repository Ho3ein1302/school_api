from django.urls import path

from . import views


app_name = 'teacher'
urlpatterns = [
    path(
        'register/',
        views.TeacherRegisterView.as_view(),
        name='register'
    ),
    path(
        'profile/<int:pk>/',
        views.TeacherProfileView.as_view(),
        name='profile'
    ),
    path(
        'homeroom/add/student/<int:pk>/',
        views.HomeRoomAddStudentView.as_view(),
        name='class-add-student'
    ),
    path(
        'news/add/',
        views.NewsView.as_view(),
        name='news-add'
    ),
    path(
        'news/update/<int:pk>/',
        views.NewsUpdateView.as_view(),
        name='news-update'
    ),
    path(
        'homework/add/',
        views.HomeWorkView.as_view(),
        name='practice-add'
    ),
    path(
        'homework/update/<int:pk>/',
        views.HomeworkUpdateView.as_view(),
        name='practice-update'
    ),
]
