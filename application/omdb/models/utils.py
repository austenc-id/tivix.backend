from . import *


class generate_id:
    def movie():
        print('init generate_id.movie()')
        medium = Medium.objects.get(name='movie')
        count = len(Production.objects.filter(medium=medium))
        new_id = count + 1
        existing = Production.objects.filter(id=new_id)
        while len(existing) > 0:
            new_id += 1
            existing = Production.objects.get(id=new_id)
        return new_id



class formatter:
    def movie(data:dict):
        try:
            medium = Medium.objects.get_or_create(
                name='movie'
                )
            audience = Audience.objects.get_or_create(
                code=data['Rated']
            )
            new_id = generate_id.movie()
            print('new_id: ', new_id)
            movie = Production.objects.create(
                id=new_id,
                medium=medium[0],
                title=data['Title'].lower(),
                date=formatter.date(data['Released']),
                description=data['Plot'],
                audience = audience[0],
                length = data['Runtime'].replace(' min', ''),
                country = data['Country'],
                awards = data['Awards'],
                poster = data['Poster'],
                earnings = formatter.earnings(data['BoxOffice'])
            )
            for genre in formatter.genres(data['Genre']):
                movie.genres.add(genre)
            for director in formatter.directors(data['Director']):
                movie.directors.add(director)
            for writer in formatter.writers(data['Writer']):
                movie.writers.add(writer)
            for actor in formatter.actors(data['Actors']):
                movie.actors.add(actor)
            for language in formatter.languages(data['Language']):
                movie.languages.add(language)
            movie.save()
            formatter.reviews(movie, data['Ratings'])

        except Exception as e:
            message = f'formatter.movie: {e}'
            print(message)
            return [message, data]
        return movie

    def date(date:str):
        try:
            date = date.split(' ')
            year = date[2]
            months = [
                ('Jan', '01'),
                ('Feb', '02'),
                ('Mar', '03'),
                ('Apr', '04'),
                ('May', '05'),
                ('Jun', '06'),
                ('Jul', '07'),
                ('Aug', '08'),
                ('Sep', '09'),
                ('Oct', '10'),
                ('Nov', '11'),
                ('Dec', '12'),
            ]
            month = date[1]
            for tup in months:
                if tup[0] == month:
                    month = tup[1]
                    break
            day = date[0]
        except Exception as e:
            message =  f'formatter.date: {e}'
            print(message)
            return message
        return f'{year}-{month}-{day}'

    def genres(data:str):
        try:
            data = data.split(',')
            genres = []
            for genre in data:
                genre = Genre.objects.get_or_create(name=genre)
                genres.append(genre[0])
        except Exception as e:
            message = f'formatter.genres: {e}'
            print(message)
            return message
        return genres

    def directors(data:str):
        try:
            data = data.split(',')
            directors = []
            for director in data:
                director = formatter.creator(director)
                director = Director.objects.get_or_create(
                    first=director[0],
                    last=director[1]
                    )
                directors.append(director[0])
        except Exception as e:
            message =  f'formatter.directors: {e}'
            print(message)
            return message
        return directors

    def writers(data:str):
        try:
            data = data.split(',')
            writers = []
            for writer in data:
                writer = formatter.creator(writer)
                writer = Writer.objects.get_or_create(first=writer[0], last=writer[1])
                writers.append(writer[0])
        except Exception as e:
            message = f'formatter.writers: {e}'
            print(message)
            return message
        return writers

    def actors(data:str):
        try:
            data = data.split(',')
            actors = []
            for actor in data:
                actor = formatter.creator(actor)
                actor = Actor.objects.get_or_create(first=actor[0], last=actor[1])
                actors.append(actor[0])
        except Exception as e:
            message = f'formatter.actors: {e}'
            print(message)
            return message
        return actors

    def creator(name:str):
        try:
            name = name.split(' ')
            first = name.pop(0)
            if first == '':
                first = name.pop(0)
            last = name.pop(0)
            while len(name) > 0:
                last += f' {name.pop(0)}'
        except Exception as e:
            message = f'formatter.creator: {e}'
            print(message)
            return message
        return (first, last)

    def languages(data:str):
        try:
            data = data.split(',')
            languages = []
            for language in data:
                language = Language.objects.get_or_create(name=language)
                languages.append(language[0])
        except Exception as e:
            message = f'formatter.languages: {e}'
            print(message)
            return message
        return languages

    def reviews(production, data:list):
        try:
            reviews = []
            for review in data:
                source = review['Source']
                value = review['Value']
                if '%' in review['Value']:
                    score = value.replace('%', '')
                    possible = 100
                else:
                    value = value.split('/')
                    score = value[0]
                    possible = value[1]
                review = Review.objects.create(
                        production=production,
                        source=source,
                        score=score,
                        possible=possible
                    )
                reviews.append(review)
        except Exception as e:
            message = f'formatter.reviews: {e}'
            print(message)
            return message
        return reviews

    def earnings(data:str):
        if data == 'N/A':
            earnings = 0
        else:
            try:
                data = data.replace('$', '')
                earnings = data.replace(',', '')
            except Exception as e:
                message = f'formatter.earnings: {e}'
                print(message)
                return message
        return earnings
