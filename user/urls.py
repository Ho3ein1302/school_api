from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path(
        'login/',
        views.UserLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.UserLogoutView.as_view(),
        name='logout'
    ),
    path(
        'token/refresh/',
        views.RefreshTokenView.as_view(),
        name='token-refresh'
    ),
]
