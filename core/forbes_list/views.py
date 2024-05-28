from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import forbesListModel
from .serializers import forbesListSerializer
from utils import common
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError, IntegrityError, transaction


# Create your views here.
class forbesListView(APIView):
    commonUtils = common.CommonUtilities()

    def get(self, request):
        """get method for forbes list"""
        """data is coming in string query"""
        year = request.query_params.get("Year", None)
        forbes_list = forbesListModel.objects.all()
        if year is not None:
            forbes_list = forbes_list.filter(Year=year)
        serializer = forbesListSerializer(forbes_list, many=True)
        return self.commonUtils.get_response(
            success=True,
            serializer=serializer,
            status_name=status.HTTP_200_OK,
            message="data successfully ",
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
                message="data saved successfully",
            )
        else:
            return self.commonUtils.get_response(
                serializer=serializer,
                status_name=status.HTTP_400_BAD_REQUEST,
                message="data could not be saved",
            )

    def delete(self, request):
        """delete method for forbes list"""
        """data is coming in payload"""
        name = request.data.get("Name")
        print("Name==", name)
        if not name:
            return self.commonUtils.get_response(
                message="name is required.",
                status_name=status.HTTP_400_BAD_REQUEST,
            )
        try:
            with transaction.atomic():
                forbes_entry = forbesListModel.objects.filter(Name=name)
        except ObjectDoesNotExist:
            return self.commonUtils.get_response(
                message="Forbes entry not found.",
                status_name=status.HTTP_404_NOT_FOUND,
            )
        except (DatabaseError, IntegrityError) as e:
            return self.commonUtils.get_response(
                message={"error in database." + str(e)},
                status_name=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        forbes_entry.delete()
        return self.commonUtils.get_response(
            success=True,
            message="data deleted successful",
            status_name=status.HTTP_204_NO_CONTENT,
        )
