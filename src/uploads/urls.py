from . import views
from django.urls import path

urlpatterns = [
    path('texts/<str:pk>', views.show_text),
    path('videos/<str:pk>', views.play_video),
    path('audio/<str:pk>', views.play_audio),
    path('audio-album/<str:pk>', views.play_audio_album),
    path('inventory/', views.faculty_view_inventory),
]
