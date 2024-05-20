from rest_framework import serializers
from .models import PlatformList, MovieList


class MovieListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    storyline = serializers.CharField(required=False, allow_blank=True, max_length=500)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return MovieList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.storyline = validated_data.get("storyline", instance.storyline)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance


class PlatformListSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    about = serializers.CharField(required=False, max_length=100)
    website = serializers.URLField()

    def create(self, validated_data):
        return PlatformList.objects.create(**validated_data)
