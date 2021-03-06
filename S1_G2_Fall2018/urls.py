"""S1_G2_Fall2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from S1_G2_Fall2018 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('searchProperty', views.searchProperty, name='searchProperty'),
    path('advertiseProperty', views.advertiseProperty, name='advertiseProperty')
]
