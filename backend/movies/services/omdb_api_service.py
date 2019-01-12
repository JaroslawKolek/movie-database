from django.conf import settings
import requests


class OMDbService:
    url_base = 'http://www.omdbapi.com/'
    api_key = settings.OMDB_API_KEY

    def __init__(self):
        self.entry_key_setup = {
            'apikey': self.api_key,
        }

    def get_movies_by_title_search(self, title, page=1):
        return self._send_get_request({
            't': title,
            'page': page
        })

    def get_movie_details_by_id(self, id):
        return self._send_get_request({
            'i': id,
        })

    def _send_get_request(self, params):
        params.update(self.entry_key_setup)
        response = requests.get(self.url_base, params)

        # if response.status_code == 200:
        #     return response.json()
        # return None
        #

        return [{
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
