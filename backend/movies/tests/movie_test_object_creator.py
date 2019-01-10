from datetime import date

from ..models import Movie, Production, Director


class MovieTestObjectCreator:
    """Class to quick-create objects from current app for testing"""
    # TODO:  Add mommy.recipe

    def create_movie(self, title, imdb_id='123', language="PL", runtime="20 min",
                     release_date=date.today(), poster_url="asd.com",
                     director=None, production=None):
        return Movie.objects.create(
            title=title,
            imdb_id=imdb_id,
            language=language,
            runtime=runtime,
            release_date=release_date,
            poster_url=poster_url,
            director=director,
            production=production
        )

    def create_director(self, name="Jarek Jarkowski"):
        return Director.objects.create(name=name)

    def create_production(self, name="Jarkowski Pictures"):
        return Production.objects.create(name=name)
