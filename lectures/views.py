from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import LectureSession, LectureNote
from .forms import LectureUploadForm
from .services import process_lecture_audio

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'lectures/register.html', {'form': form})

@login_required
def dashboard_view(request):
    sessions = LectureSession.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'lectures/dashboard.html', {'sessions': sessions})

@login_required
def upload_lecture_view(request):
    if request.method == 'POST':
        form = LectureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            
            # Run AI processing service
            transcript, summary = process_lecture_audio(session.audio_file.path)
            LectureNote.objects.create(
                session=session,
                raw_transcript=transcript,
                summary_markdown=summary
            )
            session.is_processed = True
            session.save()
            messages.success(request, 'Lecture processed and notes generated successfully!')
            return redirect('dashboard')
    else:
        form = LectureUploadForm()
    return render(request, 'lectures/upload.html', {'form': form})

@login_required
def note_detail_view(request, pk):
    session = get_object_or_404(LectureSession, pk=pk, user=request.user)
    note = get_object_or_404(LectureNote, session=session)
    return render(request, 'lectures/note_detail.html', {'session': session, 'note': note})
