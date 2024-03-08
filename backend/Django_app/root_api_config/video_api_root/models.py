from typing import Any
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CourseContaner(models.Model):
    title = models.CharField(max_length = 200)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'course_owner')
    description = models.TextField(blank = True, null = True)
    likes = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'course_object_likes', blank = True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title



class VideoMaterialContainer(models.Model):
    course = models.ForeignKey(CourseContaner, on_delete = models.CASCADE, related_name = 'course_material')
    title = models.CharField(max_length = 200)
    video_file = models.FileField(upload_to='video_files/video/')

    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
 

    def __str__(self) -> str:
        return self.title
    
    
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        self.video_file.delete()
        return super().delete(using, keep_parents)