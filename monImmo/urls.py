"""
URL configuration for monImmo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from appMonImmo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', include('monImmo.urls')),
    # path('register/', include('monImmo.urls')),
    # path('logout/', include('monImmo.urls')),
    # path('home/', include('monImmo.urls')),
    # path('property/add/', include('monImmo.urls')),
    # path('property/edit/<int:id>/', include('monImmo.urls')),
    # path('property/delete/<int:id>/', include('monImmo.urls')),
    # path('property/<int:id>/', include('monImmo.urls')),
    # path('property/', include('monImmo.urls')),
    # path('search/', include('monImmo.urls')),
    # path('contact/', monImmo.views.contact, name='contact'),
]
