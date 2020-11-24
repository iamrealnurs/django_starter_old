from django.urls import path
from task_page import views

urlpatterns = [
    path('ewq/', views.main_page, name="main_page")
]