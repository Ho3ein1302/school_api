from django.urls.conf import path

from . import views

app_name = 'school'
urlpatterns = [
    path('school/', views.SchoolView.as_view(), app_name='school-list-create'),
    path('school/detail/<int:pk>/', views.SchoolDetailView.as_view(), app_name='school-detail'),
    path('course/', views.CourseView, views.CourseView.as_view(), app_name='course-list-create'),
    path('course/detail/<int:pk>/', views.CourseDetailView.as_view(), app_name='course-detail'),
    path('homeroom/', views.HomeRoomView.as_view(), app_name='homeroom-list-create'),
    path('homeroom/detail/<int:pk>/', views.HomeRoomDetailView.as_view(), app_name='homeroom-detail')
]
