from rest_framework import serializers
from .models import MovieCollection, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = MovieCollection
        fields = ['title', 'description', 'uuid', 'movies']
