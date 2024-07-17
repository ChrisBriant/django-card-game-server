from django.urls import re_path 
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  re_path('^token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  re_path('^token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]