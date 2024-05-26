from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import forbesListModel
from .serializers import forbesListSerializer
from utils import common


# Create your views here.
class forbesListView(APIView):
    commonUtils = common.CommonUtilities()

    def get(self, request):
        """get method for forbes list"""
        year = request.query_params.get("Year", None)
        forbes_list = forbesListModel.objects.all()
        if year is not None:
            forbes_list = forbes_list.filter(Year=year)
        serializer = forbesListSerializer(forbes_list, many=True)
        return self.commonUtils.get_response(
            success=True,
            serializer=serializer,
            status_name=status.HTTP_200_OK,
        )

    def post(self, request):
        """post method for forbes list"""
        serializer = forbesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.commonUtils.get_response(
                success=True,
                serializer=serializer,
                status_name=status.HTTP_201_CREATED,
            )

        else:
            return self.commonUtils.get_response(
                success=False,
                serializer=serializer,
                status_name=status.HTTP_400_BAD_REQUEST,
            )
