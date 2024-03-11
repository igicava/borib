from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views

handler403 = 'main.views.tr_handler403'
handler404 = 'main.views.tr_handler404'
handler500 = 'main.views.tr_handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('users/', include('users.urls', namespace='users')),
    path('messenger/', include('messenger.urls', namespace='messenger')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
