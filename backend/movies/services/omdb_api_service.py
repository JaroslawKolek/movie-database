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

        if response.status_code == 200:
            return response.json()
        return None
