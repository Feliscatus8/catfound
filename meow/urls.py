from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface, name='interface'),
    path('profile/', views.profile, name='profile'),
]
