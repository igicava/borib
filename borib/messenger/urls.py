from django.urls import path, include
from messenger import views

app_name = 'messenger'

urlpatterns = [
    path('add_contact/', views.add_contact, name='add_contact'),
    path('chat/<str:recipient>/', views.chat, name='chat'),
    path('send/<str:recipienter>/', views.send, name='send'),
    path('download/', views.download_file, name='download_file'),
]
