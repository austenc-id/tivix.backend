import requests
from .keys import OMDB_KEY
from content.models import Production, Gallery


class OMDb():
    def __init__(self, query, quantity):
        self.url = f'http://www.omdbapi.com/?r=json&apikey={OMDB_KEY}'
        self.query = query
        self.quantity = quantity

    def search(self):
        url = f'{self.url}&s={self.query}'
        response = requests.get(url)
        data = response.json()
        results = self.convert(data['Search'])
        count = int(data['totalResults'])
        pages = (count // 10)
        if count % 10 > 0:
            pages += 1
        page = 2
        while len(results) < self.quantity:
            if page <= pages:
                page_results = self.next(page)
                for result in page_results:
                    results.append(result)
                page += 1
        return results

    def next(self, page):
        url = f'{self.url}&s={self.query}&page={page}'
        response = requests.get(url)
        data = response.json()
        results = self.convert(data['Search'])
        return results

    def convert(self, data):
        productions = []
        for result in data:
            try:
                production = Production.objects.get_or_create(
                    IMDBid=result['imdbID'],
                    type=result['Type'],
                    title=result['Title'],
                    year=result['Year'],
                    poster=result['Poster'],
                )
                productions.append(production[0].id)
            except:
                pass

        return productions

    def save(self, results):
        from datetime import datetime
        search = Gallery(title=datetime.now() ,type='search')
        search.save()
        all_movies = Gallery.objects.get(title='all movies')
        all_productions = Gallery.objects.get(title='all productions')
        for result in results:
            search.productions.add(result)
            all_movies.productions.add(result)
            all_productions.productions.add(result)
        search.save()
        return search