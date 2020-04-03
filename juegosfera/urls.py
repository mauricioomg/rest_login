"""juegosfera URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from apps.index.views import Login, Logout


urlpatterns = [ 
    path('admin/', admin.site.urls), 
    # Enter the app name in following syntax for this to work 
    path('', include("apps.index.urls")), 
    path('index/1.0/', include(('apps.index.urls','index'))),
    path('index_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view()),
] 