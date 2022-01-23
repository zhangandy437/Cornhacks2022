from django.urls import path

from . import views

urlpatterns = [
    path('getmp3', views.index, name = 'index'),
    path('stichedVideo', views.stitch, name = 'stitch')
]