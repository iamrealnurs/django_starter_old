from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('newest_page/', include('new_page.urls')),
    path('task_page/', include('task_page.urls')),
    path('lesson_1/', include('lesson_1.urls')),
    path('admin/', admin.site.urls),
]
