from django.urls import path
from .import views

urlpatterns = [
    path("", views.upload_resume, name="upload_resume"),
    path('download-report/<int:score>/', views.download_report, name='download_report'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),      # <--- make sure this line exists
    path('logout/', views.user_logout, name='logout'),    # <--- and this too
]
