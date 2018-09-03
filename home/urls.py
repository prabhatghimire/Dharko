"""Dharko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Service, About
# from .views import GalleryDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact,name='contact'),
    path('service/', ListView.as_view(queryset=Service.objects.all()[:25], template_name="home/service.html")),
    path('about/',ListView.as_view(queryset=About.objects.all()[:25],template_name="home/about.html")),
    path('search/', views.search,name='search'),
    # path('<int:pk>/', GalleryDetailView.as_view(), name='post'),
]
