from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import omdb

from movies.serializers.movies_serializer import MovieSerializer
from movies.models import Movie


class MoviesListView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        movies_client = omdb.OMDBClient(apikey=settings.OMDB_API_KEY)

        title = request.GET.get('title', '')
        page = request.GET.get('page', 1)

        response = {
            'movies': movies_client.search_series(title, page=page)
        }

        for movie in response.get('movies', []):
            movie_obj, _ = Movie.objects.update_or_create(
                imdb_id=movie.get('imdb_id'),
                defaults={
                    'title': movie.get('title'),
                    'poster_url': movie.get('poster')
                }
            )
        return Response(data=response)


class FavoritesMoviesListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.request.user.userdetails.favorites_movies


class FavoritesMovieView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer
    lookup_field = 'imdb_id'

    def get_queryset(self):
        return self.request.user.userdetails.favorites_movies
