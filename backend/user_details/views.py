from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movies.models import Movie


class UserFavouriteMovieManagementView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        imdb_id = request.data.get('imdb_id')
        movie = self.get_movie(imdb_id)
        if movie is None:
            return Response("Movie not found", status=HTTP_404_NOT_FOUND)

        if request.user.userdetails.favourite_movies.filter(imdb_id=imdb_id).exists():
            request.user.userdetails.favourite_movies.remove(movie)
        else:
            request.user.userdetails.favourite_movies.add(movie)
        return Response()

    def get_movie(self, imdb_id):
        if imdb_id is not None:
            return Movie.objects.filter(imdb_id=imdb_id).first()


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response("Username or password is incorrect", status=HTTP_400_BAD_REQUEST)
        return Response(Token.objects.get_or_create(user=user)[0].key)
