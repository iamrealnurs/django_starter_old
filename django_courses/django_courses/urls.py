from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kuz/', include('kuzhagaliyev_app.urls')),
    path('lesson_1/', include('lesson_1.urls')),
    path('admin/', admin.site.urls),
]
