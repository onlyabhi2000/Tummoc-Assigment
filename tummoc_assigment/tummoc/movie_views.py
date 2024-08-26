from rest_framework import status
from rest_framework.decorators import action
from .serializers import CollectionSerializer
from .models import MovieCollection, Movie
from collections import Counter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MovieCollection
from .serializers import CollectionSerializer
from .service import fetch_movies_from_api
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import MovieCollection
from .serializers import CollectionSerializer


class CollectionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        collections = MovieCollection.objects.filter(user=request.user)
        serializer = CollectionSerializer(collections, many=True)

        top_genres = self.get_top_genres(request.user)
        response_data = {
            "is_success": True,
            "data": {
                "collections": serializer.data,
                "favourite_genres": top_genres
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def get_top_genres(self, user):
        all_genres = []
        collections = MovieCollection.objects.filter(user=user).prefetch_related('movies')
        for collection in collections:
            for movie in collection.movies.all():
                all_genres.extend(movie.genres.split(', '))

        genre_counter = Counter(all_genres)
        top_3_genres = [genre for genre, count in genre_counter.most_common(3)]
        return top_3_genres

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, collection_uuid):
        try:
            collection = MovieCollection.objects.get(uuid=collection_uuid, user=request.user)
        except MovieCollection.DoesNotExist:
            return Response({'error': 'Collection not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CollectionSerializer(collection, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, collection_uuid):
        try:
            collection = MovieCollection.objects.get(uuid=collection_uuid, user=request.user)
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MovieCollection.DoesNotExist:
            return Response({'error': 'Collection not found'}, status=status.HTTP_404_NOT_FOUND)


class MoviesAPIView(APIView):
    def get(self, request):
        page = request.query_params.get('page', 1)
        movies_data = fetch_movies_from_api(page)
        if movies_data:
            return Response(movies_data, status=status.HTTP_200_OK)
        return Response({"error": "Failed to fetch movies"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
