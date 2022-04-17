from .__imports import *
from .supporting import Review

types = [
    ('movie', 'movie')
]


class Production(Model):
    id = AutoField(primary_key=True)
    IMDBid = TextField()
    type = TextField(choices=types)
    title = TextField()
    date = DateField(null=True)
    year = IntegerField()
    description = TextField(null=True)
    genres = ManyToManyField('Genre', related_name='production_genres')
    audience = TextField(null=True)
    length = IntegerField(null=True)
    directors = ManyToManyField(
        'Director', related_name='production_directors')
    writers = ManyToManyField(
        'Writer', related_name='production_writers')
    actors = ManyToManyField('Actor', related_name='production_actors')
    awards = TextField(null=True)
    poster = URLField()
    earnings = IntegerField(null=True)

    def reviews(self):
        return Review.objects.filter(production=self.id)

    def runtime(self):
        hours = self.length // 60
        if hours > 1:
            hours = f'{hours}hrs'
        else:
            hours = f'{hours}hr'
        minutes = self.length % 60
        if minutes > 1:
            minutes = f'{minutes}mins'
        else:
            minutes = f'{minutes}min'
        return hours + minutes

    def card(self):
        card = {
            'title': self.title,
            'year': self.year,
            'poster': self.poster
        }
        return card

    def credits(self):
        credits = {
            'directors': [],
            'writers': [],
            'actors': []
        }
        for director in self.directors.all():
            credits['directors'].append(director.name)
        for writer in self.writers.all():
            credits['writers'].append(writer.name)
        for actor in self.actors.all():
            credits['actors'].append(actor.name)
        return credits

    def reviews(self):
        objects = Review.objects.filter(movie=self.id)
        reviews = []
        for review in reviews:
            review = model_to_dict(review)
            reviews.append(review)
        return reviews

    def details(self):
        details = {
            'description': self.description,
            'audience': self.audience,
            'length': self.runtime(),
            'awards': self.awards,
            'earnings': self.earnings,
            'credits': self.credits(),
            'reviews': self.reviews(),
        }

        return details

    def __str__(self):
        return self.title


class Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['id', 'IMDBid', 'card', 'genres']


class DetailedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['id', 'card', 'genres', 'details']


class ViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Production.objects.all()
    serializer_class = Serializer
    permission_classes = [AllowAny]


class DetailedViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Production.objects.all()
    serializer_class = DetailedSerializer
    permission_classes = [AllowAny]
