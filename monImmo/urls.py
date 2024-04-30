from django.urls import path
from appMonImmo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('view_property/', views.view_property, name='view_property'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]