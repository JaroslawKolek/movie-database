from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import omdb

from movies.serializers import MovieSerializer
from movies.models import Movie


class MoviesSearchView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        movies_client = omdb.OMDBClient(apikey=settings.OMDB_API_KEY)

        title = request.GET.get('title', '')
        page = int(request.GET.get('page', 1))

        movies = movies_client.search_series(title, page=page)

        movies_to_return = []
        for movie in movies:
            instance, _ = Movie.objects.update_or_create(
                imdb_id=movie['imdb_id'],
                defaults={
                    'title': movie['title'],
                    'poster_url': movie['poster']
                }
            )
            movies_to_return.append(instance)
        return Response(data=MovieSerializer(movies_to_return, many=True, context={'request': request}).data)


class FavoritesMoviesListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.request.user.userdetails.favorites_movies
