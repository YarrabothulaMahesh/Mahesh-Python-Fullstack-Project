from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('register/', views.student_register, name='student_register'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
]
