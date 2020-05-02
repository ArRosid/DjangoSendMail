from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_email, name='upload_email'),
    path('send/', views.send_email, name='send_email')
]