from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    path(
        'register/',
        views.StudentRegisterView.as_view(),
        name='register'
    ),
    path(
        'profile/<int:pk>/',
        views.StudentProfileView.as_view(),
        name='register'
    ),
    path(
        'homeroom/',
        views.StudentHomeRoomView.as_view(),
        name='class'
    ),
    path(
        'news/',
        views.StudentNewsView.as_view(),
        name='news'
    ),
    path(
        'news/<int:pk>/',
        views.DetailNewsView.as_view(),
        name='detail-news'
    ),
    path(
        'homework/',
        views.StudentHomeworkView.as_view(),
        name='practice'
    ),
    path(
        'homework/<int:pk>/',
        views.DetailHomeWorkView.as_view(),
        name='detail-practice'
    ),
    path(
        'homework/response/',
        views.StudentHomeWorkResponseView.as_view(),
        name='practice-response'
    ),
    path(
        'homework/response/<int:pk>/',
        views.DetailStudentHomeWorkResponseView.as_view(),
        name='detail-practice-response'
    ),
]
