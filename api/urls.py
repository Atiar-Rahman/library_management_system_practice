

from django.urls import path
from authers.views import ViewAuthors,ViewSpecificAuthors
from publishers.views import ViewPublisher,ViewSpecificPublisher

urlpatterns = [
    path('authors/',ViewAuthors.as_view()),
    path('authors/<int:id>/',ViewSpecificAuthors.as_view()),
    path('publishers/',ViewPublisher.as_view()),
    path('publishers/<int:id>/',ViewSpecificPublisher.as_view())

]