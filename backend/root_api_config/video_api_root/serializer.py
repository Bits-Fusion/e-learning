
# rest frame work imports
from rest_framework import serializers


# project imports
from .models import CourseContaner, VideoMaterialContainer



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContaner
        fields = [
            "title",
            "owner", 
            "description", 
            "likes"
        ]



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterialContainer
        fields = [
            "course",
            "title",
            "video_file"
        ]