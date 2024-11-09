from django.urls import path
from . views import add_authors
urlpatterns = [
    path('add/',add_authors,name='add_authors')
]
