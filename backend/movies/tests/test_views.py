from unittest.mock import MagicMock, patch
from rest_framework.test import APITestCase
from django.shortcuts import reverse

from movies.models import Movie
from user_details.utils import create_test_user_and_user_details

from .omdb_api_response import OMDB_CORRECT_RESPONSE


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


class MoviesSearchViewTestCase(APITestCase):
    """ Favorites Movies Search View Test Case """

    def setUp(self):
        self.user = create_test_user_and_user_details('username', 'password')[0]
        self.url = reverse('movies:search-movies')

    def test_permissions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    @patch('movies.views.omdb')
    def test_search_movie_for_creating_all_movies(self, omdb_mock):
        Movie.objects.all().delete()
        self.client.force_authenticate(self.user)
        omdb_mocked_instance = self._mocked_omdb(omdb_mock)

        response = self.client.get(self.url, data={'title': 'Bond', 'page': 1})

        self.assertEqual(response.status_code, 200)
        omdb_mocked_instance.search_series.assert_called_with('Bond', page=1)
        self.assertEqual(len(response.json()), len(OMDB_CORRECT_RESPONSE))
        self.assertEqual(Movie.objects.all().count(), len(OMDB_CORRECT_RESPONSE))
        for movie_json in response.json():
            movie_from_db = Movie.objects.get(imdb_id=movie_json['imdb_id'])
            self.assertEqual(movie_from_db.title, movie_json['title'])
            self.assertEqual(movie_from_db.poster_url, movie_json['poster_url'])

    @patch('movies.views.omdb')
    def test_search_movie_for_updating_all_movies(self, omdb_mock):
        for movie_json in OMDB_CORRECT_RESPONSE:
            Movie.objects.create(imdb_id=movie_json['imdb_id'])
        self.assertEqual(Movie.objects.all().count(), len(OMDB_CORRECT_RESPONSE))

        self.client.force_authenticate(self.user)
        omdb_mocked_instance = self._mocked_omdb(omdb_mock)
        response = self.client.get(self.url, data={'title': 'Bond', 'page': 1})

        self.assertEqual(response.status_code, 200)
        omdb_mocked_instance.search_series.assert_called_with('Bond', page=1)
        self.assertEqual(len(response.json()), len(OMDB_CORRECT_RESPONSE))
        self.assertEqual(Movie.objects.all().count(), len(OMDB_CORRECT_RESPONSE))
        for movie_json in response.json():
            movie_from_db = Movie.objects.get(imdb_id=movie_json['imdb_id'])
            self.assertEqual(movie_from_db.title, movie_json['title'])
            self.assertEqual(movie_from_db.poster_url, movie_json['poster_url'])

    @patch('movies.views.omdb')
    def test_if_page_number_is_passed_correctly(self, omdb_mock):
        self.client.force_authenticate(self.user)
        omdb_mocked_instance = self._mocked_omdb(omdb_mock)
        response = self.client.get(self.url, data={'title': 'Bond', 'page': 2})

        self.assertEqual(response.status_code, 200)
        omdb_mocked_instance.search_series.assert_called_with('Bond', page=2)

    def _mocked_omdb(self, omdb_mock):
        omdb_mocked_instance = MagicMock(
            name='omdb_instance_mocked', search_series=MagicMock(return_value=OMDB_CORRECT_RESPONSE)
        )
        omdb_mock.OMDBClient.return_value = omdb_mocked_instance
        return omdb_mocked_instance
