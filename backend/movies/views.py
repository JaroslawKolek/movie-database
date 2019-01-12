from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services.omdb_api_service import OMDbService
from .serializers.movies_serializer import MovieSerializer
from .models import Movie, Production


class MoviesListView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        omdb_service = OMDbService()
        title = request.GET.get('title', '')
        page = request.GET.get('page', 1)

        response = {
            'movies': omdb_service.get_movies_by_title_search(title, page)
        }

        for movie in response.get('movies', []):
            production, _ = Production.objects.get_or_create(name=movie.get('Production'))
            movie_obj, _ = Movie.objects.update_or_create(
                imdb_id=movie.get('imdbID'),
                defaults={
                    'title': movie.get('Title'),
                    'production': production
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
