from django.urls import path
from users.views import login, register, profile, profile_edit, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('logout/', user_logout, name='logout'),
]

