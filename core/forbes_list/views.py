from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import forbesListModel
from .serializers import forbesListSerializer


# Create your views here.
class forbesListView(APIView):
    def get(self, request):
        forbesList = forbesListModel.objects.all()
        serializer = forbesListSerializer(forbesList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
