import mimetypes
import os
from urllib.parse import unquote


from django.conf import settings
from django.http import FileResponse


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import CourseContaner, VideoMaterialContainer
from .serializer import CourseSerializer, VideoSerializer



class CourseCreateAndGetAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = CourseContaner.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CourseUpdateDeleteAndGetAPIView(generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = CourseContaner
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class VideoCreateAndGetAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = VideoMaterialContainer.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]


class VideoUpdateDeleteAndGetAPIView(generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = VideoMaterialContainer
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]