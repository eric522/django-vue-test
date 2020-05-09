from rest_framework import generics, views, status
from rest_framework.response import Response
from .serializers import Tag, Movie, TagSerializer, MovieSerializer
from django.http import Http404

# Create your views here.
class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TagDetail(views.APIView):

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieDetail(views.APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)