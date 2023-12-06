from django.urls import path, include


# 3rd party packeges
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# My view applications
from .views import (
    UserLoginView,
    UserSignUpView,
    UserLogOut,
    ProfileUpdate,
    ProfileDamp
)


urlpatterns = [
    # JWt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # basic login, sign in and logout pages
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('signup/', UserSignUpView.as_view(), name='signup'),

    # update profile
    path('profile/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<str:user_name>/',  ProfileDamp.as_view(), name='profile_info'),
    
]