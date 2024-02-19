# django imports
from django.urls import path

#3rd party
from drf_social_oauth2.urls import TokenView
from drf_social_oauth2.urls import RevokeTokenView

# project view applications
from .views import (
    UserSignUpAPIView,
    UserInformationRetrieveAPIView,
    UserProfileUpdateAPIView,
    get_media_path,
)


urlpatterns = [
    # basic login, sign in and logout pages
    path('signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('login/' , TokenView.as_view() , name='login'),

    # update profile
    path('profile/update/<str:username>/', UserProfileUpdateAPIView.as_view(), name='profile_update_by_serializer'),

    # dump user information if needed
    path('profile/<str:username>/',  UserInformationRetrieveAPIView.as_view(), name='profile_info'),
    path("media/<str:path>", get_media_path, name="get-media-path"),
    
]