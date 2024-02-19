# django imports
from django.urls import path


# project view applications
from .views import (
    CourseCreateAndGetAPIView,
    CourseUpdateDeleteAndGetAPIView,

    VideoCreateAndGetAPIView,
    VideoUpdateDeleteAndGetAPIView,
)


urlpatterns = [
    path('', CourseCreateAndGetAPIView.as_view(), name='get_course'),
    path('create/', CourseCreateAndGetAPIView.as_view(), name='create_course'),
    path('update/<str:id>/', CourseUpdateDeleteAndGetAPIView.as_view(), name="update-course"),
    path('get/<str:id>/', CourseUpdateDeleteAndGetAPIView.as_view(), name="get-course"),
    path('delete/<str:id>/', CourseUpdateDeleteAndGetAPIView.as_view(), name="delete-course"),

    path('video/', VideoCreateAndGetAPIView.as_view(), name='get_video'),
    path('video/create/', VideoCreateAndGetAPIView.as_view(), name='vedio_course'),
    path('video/update/<str:id>/', VideoUpdateDeleteAndGetAPIView.as_view(), name="video-course"),
    path('video/get/<str:id>/', VideoUpdateDeleteAndGetAPIView.as_view(), name="video-course"),
    path('video/delete/<str:id>/', VideoUpdateDeleteAndGetAPIView.as_view(), name="video-course"),
]