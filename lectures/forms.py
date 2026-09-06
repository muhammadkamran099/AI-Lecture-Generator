from django import forms
from .models import LectureSession

class LectureUploadForm(forms.ModelForm):
    class Meta:
        model = LectureSession
        fields = ['title', 'audio_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lecture title...'}),
            'audio_file': forms.FileInput(attrs={'class': 'form-control'})
        }
