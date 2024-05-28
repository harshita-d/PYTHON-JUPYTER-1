from rest_framework.response import Response
from rest_framework import status


class CommonUtilities:

    def get_response(self, success=False, serializer=None, status_name="", message=""):
        """method to get response on call of API"""
        error_messages = (
            [
                f"{field}: {error}"
                for field, errors in serializer.errors.items()
                for error in errors
            ]
            if not success and serializer and hasattr(serializer, 'errors')
            else []
        )
        error_response = {
            "success": success,
            "status": status_name,
            "errors": error_messages,
            "message": message,
            "data": serializer.data if serializer else [],
        }
        return Response(error_response, status=status_name)
