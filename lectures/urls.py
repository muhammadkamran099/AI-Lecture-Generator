from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('upload/', views.upload_lecture_view, name='upload_lecture'),
    path('note/<int:pk>/', views.note_detail_view, name='note_detail'),
    path('register/', views.register_view, name='register'),
]
