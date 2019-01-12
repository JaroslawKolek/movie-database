from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services.omdb_api_service import OMDbService
from .serializers.movies_serializer import MovieSerializer


class MoviesListView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        # omdb_service = OMDbService()
        #
        # title = request.GET.get('title')
        # page = request.GET.get('page', 1)
        #
        # if not title:
        #     Response("Title param is mandatory!", status=400)
        #
        # return Response({
        #     'movies': omdb_service.get_movies_by_title_search(title, page)
        # })
        response = {
            'movies': [{
                "Title": "X-Men",
                "Year": "2000",
                "Rated": "PG-13",
                "Released": "14 Jul 2000",
                "Runtime": "104 min",
                "Genre": "Action, Adventure, Sci-Fi",
                "Director": "Bryan Singer",
                "Writer": "Tom DeSanto (story), Bryan Singer (story), David Hayter (screenplay)",
                "Actors": "Hugh Jackman, Patrick Stewart, Ian McKellen, Famke Janssen",
                "Plot": "Two mutants come to a private academy for their kind whose resident superhero team must oppose a terrorist organization with similar powers.",
                "Language": "English",
                "Country": "USA",
                "Awards": "13 wins & 26 nominations.",
                "Poster": "https://m.media-amazon.com/images/M/MV5BZmJkOGY4YjYtM2FmYy00MTIyLTg2YTUtMzJiNjljMWM5MGUwXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_SX300.jpg",
                "Ratings": [
                    {
                        "Source": "Internet Movie Database",
                        "Value": "7.4/10"
                    },
                    {
                        "Source": "Rotten Tomatoes",
                        "Value": "81%"
                    },
                    {
                        "Source": "Metacritic",
                        "Value": "64/100"
                    }
                ],
                "Metascore": "64",
                "imdbRating": "7.4",
                "imdbVotes": "520,792",
                "imdbID": "tt0120903",
                "Type": "movie",
                "DVD": "21 Nov 2000",
                "BoxOffice": "$156,164,829",
                "Production": "20th Century Fox",
                "Website": "http://www.x-men-the-movie.com",
                "Response": "True"
            }]
        }
        for movie in response.get('movies', []):
            pass
            # with transaction.atomic():
            #     # get or create by idF
            #     # do update
            # # TODO get or create
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
