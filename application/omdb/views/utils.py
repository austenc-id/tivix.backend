import requests
from django.shortcuts import redirect
from config.settings._secrets import OMDB_KEY
from omdb.models import formatter, Search
from django.http.response import HttpResponse, JsonResponse


def tracker(current):
    print(current)
    return current + 1


class search:
    base = f'http://www.omdbapi.com/?r=json&apikey={OMDB_KEY}'

    def movie(name: str):
        url = f'{search.base}&type=movie&t={name}'
        response = requests.get(url)
        status = response.status_code
        data = response.json()
        try:
            message = data['Error']
            return {'message': message}
        except:
            movie = formatter.movie(data)
            return {'movie': movie}

    def movies(request, query: str):
        url = f'{search.base}&type=movie&s={query}'
        response = requests.get(url)
        status = response.status_code
        data = response.json()
        content = data['Search']
        count = int(data['totalResults'])
        for movie in data['Search']:
            try:
                movie = search.movie(movie)
            except:
                pass
        if count > 10:
            url = f'{search.base}&type=movie&s={query}&page=2'
            response = requests.get(url)
            data = response.json()
            for result in data['Search']:
                content.append(result)
                try:
                    movie = search.movie(movie)
                except:
                    pass
        try:
            new_search = Search(content=content, count=len(
                data['Search']), total=data['totalResults'])
            new_search.save()
        except:
            pass
        return JsonResponse({'results': new_search.id})
