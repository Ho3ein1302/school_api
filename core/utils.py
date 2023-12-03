from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# JWT Token
def get_tokens(user) -> dict:
    """
        The function "get_tokens()" takes in "user" and returns a "dict".
        The "dict" gives us 'access token' and 'refresh token'.
    """
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }


# Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="School API",
      default_version='v1',
      description="school API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
