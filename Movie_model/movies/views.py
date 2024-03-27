from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
from django.core.paginator import Paginator

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movie_type = 'action')
    serializer_class = MovieSerializer

class ComedyViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movie_type = 'comedy')
    serializer_class = MovieSerializer

def movie_list(request):
    movies_objects = Moviedata.objects.all()
    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movies_objects = movies_objects.filter(name__icontains = movie_name)
    
    paginator = Paginator(movies_objects, 4)
    page = request.GET.get('page')
    movies_objects = paginator.get_page(page)
    
    return render(request, 'movies/movie_list.html', {'movies_objects' : movies_objects})