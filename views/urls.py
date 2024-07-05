from django.urls import path

from . import views

urlpatterns = [
    path('weather/', views.get_weather, name='get_weather'),
    path('test_cache/', views.test_cache, name='test_cache'),
]