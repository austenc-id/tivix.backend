import requests
from config.settings._secrets import OMDB_KEY
from omdb.models import formatter


def tracker(current):
    print(current)
    return current + 1


class requester:
    base = f'http://www.omdbapi.com/?r=json&apikey={OMDB_KEY}'
    def movie(name):
        url = f'{requester.base}&type=movie&t={name}'
        response = requests.get(url)
        status = response.status_code
        data = response.json()
        try:
            message = data['Error']
            return {'message': message}
        except:
            movie = formatter.movie(data)
            return {'movie': movie}
