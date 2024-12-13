from django.urls import path
from . views import add_categories
urlpatterns = [
    path('add/',add_categories,name='add_category')
]