from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from publishers.models import Publishers
from publishers.serializers import PublisherSerializer

# Create your views here.
class ViewPublisher(ListCreateAPIView):
    queryset = Publishers.objects.all()
    serializer_class = PublisherSerializer


class ViewSpecificPublisher(RetrieveUpdateDestroyAPIView):
    queryset = Publishers.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'id'