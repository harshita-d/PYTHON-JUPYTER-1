from rest_framework import serializers
from .models import PlatformList, MovieList


class MovieListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    storyline = serializers.CharField(required=False, allow_blank=True, max_length=500)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return MovieList.objects.create(**validated_data)
