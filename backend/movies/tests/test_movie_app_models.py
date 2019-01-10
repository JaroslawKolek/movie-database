from django.test import TestCase

from ..models import Movie, Director, Production
from .movie_test_object_creator import MovieTestObjectCreator


class MoviesAppModelsTestCase(TestCase, MovieTestObjectCreator):
    """ Basic Models tests from Movies App """

    def setUp(self):
        self.movie_1 = self.create_movie("Movie 1")
        self.director_1 = self.create_director()
        self.production_1 = self.create_production()

    def test_if_movie_created(self):
        self.assertEqual(Movie.objects.count(), 1)

    def test_if_director_created(self):
        self.assertEqual(Director.objects.count(), 1)

    def test_if_production_created(self):
        self.assertEqual(Production.objects.count(), 1)

    def test_if_movie_connects_with_fk(self):
        self.movie_1.director = self.director_1
        self.movie_1.production = self.production_1
        self.movie_1.save()

        movie_from_db = Movie.objects.get(id=self.movie_1.id)

        self.assertEqual(movie_from_db.director, self.director_1)
        self.assertEqual(movie_from_db.production, self.production_1)
