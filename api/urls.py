

from django.urls import path
from authers.views import authers_view,view_specific_authors

urlpatterns = [
    path('authors/',authers_view),
    path('authors/<int:pk>/',view_specific_authors)
]