from rest_framework.serializers import ModelSerializer

from .models import forbesListModel


class forbesListSerializer(ModelSerializer):
    """forbes list serializer"""

    class Meta:
        model = forbesListModel
        fields = ["id", "Name", "Pay_USD", "Year", "Category"]

