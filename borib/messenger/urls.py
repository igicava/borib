from django.urls import path, include
from messenger import views

app_name = 'messenger'

urlpatterns = [
    path('send/', views.send),
    path('add_contact/', views.add_contact)
]
