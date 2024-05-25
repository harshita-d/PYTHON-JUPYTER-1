from rest_framework import serializers
from .models import PlatformList, MovieList


class MovieListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Poster_Link = serializers.URLField(max_length=100)
    Series_Title = serializers.CharField(max_length=100)
    Released_Year = serializers.IntegerField()
    Certificate = serializers.CharField(max_length=100)
    Runtime = serializers.CharField(max_length=100)
    Genre = serializers.CharField(max_length=100)
    IMDB_Rating = serializers.IntegerField()
    Overview = serializers.CharField(max_length=1000)
    Director = serializers.CharField(max_length=100)
    Star1 = serializers.CharField(max_length=100)
    Star2 = serializers.CharField(max_length=100)
    Star3 = serializers.CharField(max_length=100)
    Star4 = serializers.CharField(max_length=100)
    Gross = serializers.CharField(max_length=500)

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
