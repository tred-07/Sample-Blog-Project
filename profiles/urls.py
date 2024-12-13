from django.urls import path
from . views import add_profiles
urlpatterns = [
    path('add/',add_profiles,name='add_profiles')
]