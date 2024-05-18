from django.http import HttpResponse, JsonResponse
from .models import PlatformList, MovieList
from .serializers import MovieListSerializer


def movieListView(request):
    movies = MovieList.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)
