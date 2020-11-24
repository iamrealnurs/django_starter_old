from django.urls import path
from kuzhagaliyev_app import views

urlpatterns = [
    path('', views.nursultan),
    path('bro', views.turlan),
]
