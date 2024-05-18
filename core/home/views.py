from django.http import HttpResponse, JsonResponse
from .models import PlatformList, MovieList
from .serializers import MovieListSerializer, PlatformListSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def movieListView(request):
    print(request)
    if request.method == "GET":
        movies = MovieList.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        print("data:- ", data)
        postSerializer = MovieListSerializer(data=data)
        if postSerializer.is_valid():
            postSerializer.save()
            return JsonResponse(postSerializer.data, status=201)
        return JsonResponse(postSerializer.errors, status=400)


def platformListView(request):
    platformModal = PlatformList.objects.all()
    serializer = PlatformListSerializer(platformModal, many=True)
    return JsonResponse(serializer.data, safe=False)
