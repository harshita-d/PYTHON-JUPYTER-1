from rest_framework.response import Response
from rest_framework import status


class CommonUtilities:

    def get_response(self, success, serializer, status_name):
        """method to get response on call of API"""
        success_message = "successful"
        failure_message = "failed"
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
            "message": success_message if success else failure_message,
            "data": serializer.data,
        }
        return Response(error_response, status=status_name)
