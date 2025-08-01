

from django.urls import path
from authers.views import ViewAuthors,ViewSpecificAuthors

urlpatterns = [
    path('authors/',ViewAuthors.as_view()),
    path('authors/<int:id>/',ViewSpecificAuthors.as_view())
]