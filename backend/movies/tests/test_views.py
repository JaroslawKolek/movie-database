from rest_framework.test import APITestCase
from django.shortcuts import reverse

from movies.models import Movie
from user_details.utils import create_test_user_and_user_details


class FavoritesMoviesListViewTestCase(APITestCase):
    """ Favorites Movies List View Test Case """

    fixtures = ['movies']

    def setUp(self):
        self.user = create_test_user_and_user_details('username', 'password')[0]
        self.url = reverse('movies:favorites-movies-list')
        for movie in Movie.objects.all()[:3]:
            self.user.userdetails.favorites_movies.add(movie)

    def test_permissions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_list_favorite_movies(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), self.user.userdetails.favorites_movies.count())
        for movie in response.json():
            self.assertTrue(self.user.userdetails.favorites_movies.filter(imdb_id=movie['imdb_id']).exists())
