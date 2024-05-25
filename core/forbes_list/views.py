from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import forbesListModel
from .serializers import forbesListSerializer


# Create your views here.
class forbesListView(APIView):
    def get(self, request):
        year = request.query_params.get("Year", None)
        forbes_list = forbesListModel.objects.all()
        if year is not None:
            forbes_list = forbes_list.filter(Year=year)
        serializer = forbesListSerializer(forbes_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
