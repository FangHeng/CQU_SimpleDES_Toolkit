"""CQU_SimpleDES_Toolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Cipher import views

app_name = "Cipher"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.start),
    path("index/", views.index),
    path("plaintext_sent/", views.plaintext_sent),
    path("ciphertext_sent/",views.ciphertext_sent)

]
