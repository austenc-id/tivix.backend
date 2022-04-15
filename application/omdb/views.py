import requests
from django.shortcuts import render
from ._secrets import personal_key
from .models import *

def fetch_data(request, media, name):

    base_url = f'http://www.omdbapi.com/?r=json&apikey={personal_key}&type={media}&t={name}'
    response = requests.get(base_url)
    status = response.status_code
    content = response.json()
    if media == 'movie':
        production = get_movie(content)
    else:
        production = 'media type not supported'
    context = {
        'status': status,
        'production': production,
        'content': content,
    }

    return render(request, 'response.html', context)

def get_movie(content):
    medium = Medium.objects.get_or_create(name='movie')
    date = content['Released'].split(' ')
    date = format_date(date)
    genres = content['Genre'].split(',')
    genre_objs = []
    for genre in genres:
        genre = Genre.objects.get_or_create(name=genre)
        genre_objs.append(genre[0])
    # 'code name desc'
    audience = MPA_Rating.objects.get_or_create(code=content['Rated'])
    length = content['Runtime'].replace(' min', '')
    # 'first middle last'
    directors = content['Director'].split(',')
    directors = create_creators(directors, directors=True)
    writers = content['Writer'].split(',')
    writers = create_creators(writers, writers=True)
    actors = content['Actors'].split(',')
    actors = create_creators(actors, actors=True)
    # 'name abr'
    languages = content['Language'].split(',')
    language_objs = []
    for language in languages:
        language = Language.objects.get_or_create(name=language)
        language_objs.append(language[0])
    # 'source score possible sample'
    reviews = content['Ratings']
    review_objs = []
    for review in reviews:
        source = review['Source']
        value = review['Value']
        if '%' in value:
            score = value.replace('%', '')
            possible = 100
        else:
            value = value.split('/')
            score = value[0]
            possible = value[1]
        review = Rating.objects.get_or_create(source=source, score=score, possible=possible, sample_size=0)
        review_objs.append(review[0])
    box_office = content['BoxOffice'].replace('$', '')
    box_office = box_office.replace(',', '')
    data = [
        medium[0],
        content['Title'],
        date,
        content['Plot'],
        genre_objs,
        audience[0],
        length,
        directors,
        writers,
        actors,
        language_objs,
        content['Country'],
        content['Awards'],
        content['Poster'],
        review_objs,
        box_office
    ]
    return create_production(data)

def format_date(date:list):
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
    return f'{year}-{month}-{day}'

def create_creators(names:list, directors=False, writers=False, actors=False):
    creators = []
    try:
        for name in names:
            name = name.split(' ')
            first = name.pop(0)
            if first == '':
                first = name.pop(0)
            if len(name) == 1:
                last = name.pop(0)
                if directors:
                    creator = Director.objects.get_or_create(first=first, last=last)
                elif writers:
                    creator = Writer.objects.get_or_create(first=first, last=last)
                elif actors:
                    creator = Actor.objects.get_or_create(first=first, last=last)
                creators.append(creator[0])
            else:
                middle = name.pop(0)
                last = name.pop(0)
                while len(name) > 0:
                    last += ' ' + name.pop(0)
                if directors:
                    creator = Director.objects.get_or_create(first=first, middle=middle, last=last)
                elif writers:
                    creator = Writer.objects.get_or_create(first=first, middle=middle, last=last)
                elif actors:
                    creator = Actor.objects.get_or_create(first=first, middle=middle, last=last)
                creators.append(creator[0])
    except Exception as e:
        return e
    return creators

def create_production(data):
    try:
        production = Production.objects.get_or_create(
            medium = data[0],
            title=data[1],
            date=data[2],
            description=data[3],
            audience=data[5],
            length=data[6],
            country=data[11],
            awards=data[12],
            poster=data[13],
            box_office=data[15]
        )
        existing = production[1]
        production = production[0]
        if not existing:
            for genre in data[4]:
                production.genres.add(genre)
            for director in data[7]:
                production.directors.add(director)
            for writer in data[8]:
                production.writers.add(writer)
            for actor in data[9]:
                production.actors.add(actor)
            for language in data[10]:
                production.languages.add(language)
            for review in data[14]:
                production.reviews.add(review)
            production.save()
    except Exception as e:
        return e
    return production

            # genres=data[4],
            # directors=data[7],
            # writers=data[8],
            # actors=data[9],
            #             languages=data[10],
            # reviews=data[14],
