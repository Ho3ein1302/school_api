from django.urls.conf import path

from . import views

app_name = 'core'
urlpatterns = [
    path(
        '',
        views.SchoolView.as_view(),
        name='school-list-create'
    ),
    path(
        '/detail/<int:pk>/',
        views.SchoolDetailView.as_view(),
        name='school-detail'
    ),
    path(
        'course/',
        views.CourseView.as_view(),
        name='course-list-create'
    ),
    path(
        'course/detail/<int:pk>/',
        views.CourseDetailView.as_view(),
        name='course-detail'
    ),
    path(
        'homeroom/',
        views.HomeRoomView.as_view(),
        name='homeroom-list-create'
    ),
    path(
        'homeroom/detail/<int:pk>/',
        views.HomeRoomDetailView.as_view(),
        name='homeroom-detail'
    )
]
