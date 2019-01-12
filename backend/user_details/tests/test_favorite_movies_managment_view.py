from django.shortcuts import reverse
from rest_framework.test import APITestCase
from movies.models import Movie
from user_details.utils import create_test_user_and_user_details


class UserFavoriteMoviesManagementView(APITestCase):
    """ Test User favorite movies """

    fixtures = ['movies']

    def setUp(self):
        self.username = "username"
        self.password = "password"
        self.user, _ = create_test_user_and_user_details(self.username, self.password)

    def test_permissions(self):
        movie_to_add = Movie.objects.all()[0]
        response = self._put_favorite_movie(movie_to_add.imdb_id)
        self.assertEqual(response.status_code, 401)

    def test_adding_movie_as_favorite_when_it_does_not_exist(self):
        non_existing_imdb_id = 'non-existing'
        self.client.force_authenticate(self.user)
        response = self._put_favorite_movie(non_existing_imdb_id)
        self.assertEqual(response.status_code, 404)

    def test_adding_movie_as_favorite(self):
        self.assertEqual(self.user.userdetails.favorites_movies.all().count(), 0)
        self.client.force_authenticate(self.user)
        movie_to_add = Movie.objects.all()[0]
        response = self._put_favorite_movie(movie_to_add.imdb_id)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.userdetails.favorites_movies.all().count(), 1)
        self.assertEqual(self.user.userdetails.favorites_movies.all()[0].pk, movie_to_add.pk)

    def test_removing_movie_from_favorite(self):
        fav_movie = Movie.objects.all()[0]
        self.user.userdetails.favorites_movies.add(fav_movie)
        self.assertEqual(self.user.userdetails.favorites_movies.all().count(), 1)
        self.client.force_authenticate(self.user)
        response = self._put_favorite_movie(fav_movie.imdb_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.userdetails.favorites_movies.all().count(), 0)

    def _put_favorite_movie(self, movie_imdb_id):
        url = reverse('user_details:manage-favorite-movies')
        return self.client.put(url, data={'imdb_id': movie_imdb_id})
