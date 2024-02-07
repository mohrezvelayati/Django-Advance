from django.urls import path
from .. import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # Registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),

    
    # Change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),
    
    # Reset password
    
    # Login token
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login' ),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout' ),

    # Login jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

]

