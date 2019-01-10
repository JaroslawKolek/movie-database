from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services.omdb_api_service import OMDbService


class MoviesView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        omdb_service = OMDbService()

        title = request.GET.get('title')
        page = request.GET.get('page', 1)

        if not title:
            Response("Title param is mandatory!", status=400)

        return Response({
            'movies': omdb_service.get_movies_by_title_search(title, page)
        })


class FavoritesMoviesView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_fav_movies = request.user.userdetails.favorites_movies.all()

        return Response({
            'movies': user_fav_movies
        })

    def post(self, request):
        pass
