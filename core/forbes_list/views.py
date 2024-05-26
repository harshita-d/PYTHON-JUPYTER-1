from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import forbesListModel
from .serializers import forbesListSerializer


# Create your views here.
class forbesListView(APIView):
    sucess_message = "data has been saved successfully"

    def get_response(self, success, serializer, status_name):
        error_messages = (
            [
                f"{field}: {error}"
                for field, errors in serializer.errors.items()
                for error in errors
            ]
            if not success
            else []
        )
        error_response = {
            "success": success,
            "status": status_name,
            "errors": error_messages,
            "message": "Validation Successful" if success else "Validation failed",
            "data": serializer.data,
        }
        return Response(error_response, status=status_name)

    def get(self, request):
        year = request.query_params.get("Year", None)
        forbes_list = forbesListModel.objects.all()
        if year is not None:
            forbes_list = forbes_list.filter(Year=year)
        serializer = forbesListSerializer(forbes_list, many=True)
        return self.get_response(
            success=True,
            serializer=serializer,
            status_name=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = forbesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_response(
                success=True,
                serializer=serializer,
                status_name=status.HTTP_201_CREATED,
            )

        else:
            return self.get_response(
                success=False,
                serializer=serializer,
                status_name=status.HTTP_400_BAD_REQUEST,
            )
