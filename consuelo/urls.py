"""consuelo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from webpages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', register_view, name="signup"),
    path('accounts/settings/', settings_view, name="settings"),
    path('accounts/bookings/', bookings_view, name="bookings"),
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('services/', services_view, name="services"),
    path('services/traditional_therapy', traditional_therapy_view, name="traditional_therapy"),
    path('contact/', contact_view, name="contact")
]
