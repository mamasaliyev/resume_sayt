from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),

]