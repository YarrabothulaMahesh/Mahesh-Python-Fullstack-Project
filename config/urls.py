"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Job Portal Homepage
    path('', include('accounts.urls')),
]