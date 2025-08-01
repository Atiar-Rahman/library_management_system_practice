from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from authers.serializers import AuthorSerializer
from authers.models import Authors
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

@api_view(['GET', 'POST'])
def authers_view(request):
    if request.method=='GET':
        authers = Authors.objects.all()
        print(authers)
        serialiser = AuthorSerializer(authers,many=True)
        return Response(serialiser.data)
    if request.method == 'POST':
        serialiser = AuthorSerializer(data = request.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
    return Response(serialiser.data)

@api_view(['GET','PUT','PATCH','DELETE'])
def view_specific_authors(request,pk):
    author = get_object_or_404(Authors,pk=pk)
    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = AuthorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method=='PATCH':
        serializer = AuthorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        author.delete()
        return Response("successfully")
    

# convert classbased view

# class ViewAuthors(APIView):
#     def get(self,request):
#         authors = Authors.objects.all()
#         serilizer = AuthorSerializer(authors,many = True)
#         return Response(serilizer.data)
    
#     def post(self,request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class ViewAuthors(ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

class ViewSpecificAuthors(RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'