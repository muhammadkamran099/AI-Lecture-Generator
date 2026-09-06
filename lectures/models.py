from django.db import models
from django.contrib.auth.models import User

class LectureSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='lecture_audio/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class LectureNote(models.Model):
    session = models.OneToOneField(LectureSession, on_delete=models.CASCADE)
    raw_transcript = models.TextField(blank=True, null=True)
    summary_markdown = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notes: {self.session.title}"
