from django.http import HttpResponse, JsonResponse
from .models import PlatformList, MovieList
from .serializers import MovieListSerializer, PlatformListSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def movieListView(request):
    if request.method == "GET":
        movies = MovieList.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        postSerializer = MovieListSerializer(data=data)
        if postSerializer.is_valid():
            postSerializer.save()
            return JsonResponse(postSerializer.data, status=201)
        return JsonResponse(postSerializer.errors, status=400)


def movieListIndexView(request, pk):
    movies = MovieList.objects.get(pk=pk)
    serializer = MovieListSerializer(movies)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def platformListView(request):
    if request.method == "GET":
        platformModal = PlatformList.objects.all()
        serializer = PlatformListSerializer(platformModal, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PlatformListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


def platformListIndexView(request, pk):
    platformModal = PlatformList.objects.get(pk=pk)
    serializer = PlatformListSerializer(platformModal)
    return JsonResponse(serializer.data, safe=False)
