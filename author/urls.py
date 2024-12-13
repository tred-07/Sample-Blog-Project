from django.urls import path
from . views import add_authors,confAuthor
urlpatterns = [
    path('add/',add_authors,name='add_authors'),
    # path('',confAuthor,name='home')
]
