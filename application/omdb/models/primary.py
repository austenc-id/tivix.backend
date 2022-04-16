from django.db import models
from django.forms.models import model_to_dict
from .supporting import Medium, Genre, Audience, Director, Writer, Actor, Language


class Gallery(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    title = models.CharField(max_length=48)
    description = models.TextField()
    productions = models.ManyToManyField('Production', blank=True,related_name='gallery_productions')

    def to_dict(self):
        return model_to_dict(self)


class Production(models.Model):
    id = models.AutoField(primary_key=True)
    medium = models.ForeignKey(Medium, null=True, on_delete=models.SET_NULL, related_name='production_edium')
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='production_genres')
    audience = models.ForeignKey(Audience, null=True, on_delete=models.SET_NULL, related_name='production_audience')
    length = models.IntegerField()
    directors = models.ManyToManyField(Director, related_name='production_directors')
    writers = models.ManyToManyField(Writer, related_name='production_writers')
    actors = models.ManyToManyField(Actor, related_name='production_actors')
    languages = models.ManyToManyField(Language, related_name='production_languages')
    country = models.CharField(max_length=48)
    awards = models.TextField()
    poster = models.URLField()
    earnings = models.IntegerField()

    def year(self):
        return self.date.year

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
        return  hours + minutes

    def __str__(self):
        return self.title

    def to_dict(self):
        production = {
            'id': self.id,
            'medium': self.medium.to_dict(),
            'title': self.title,
            'date': self.date,
            'year': self.year(),
            'description': self.description,
            'genres': [],
            'audience': self.audience.to_dict(),
            'length': self.length,
            'runtime': self.runtime(),
            'directors': [],
            'writers': [],
            'actors': [],
            'languages': [],
            'awards': self.awards,
            'poster': self.poster,
            'reviews': [],
            'earnings': self.earnings
        }
        for genre in self.genres.all():
            genre = genre.to_dict()
            production['genres'].append(genre)
        for director in self.directors.all():
            director = director.to_dict()
            production['directors'].append(director)
        for writer in self.writers.all():
            writer = writer.to_dict()
            production['writers'].append(writer)
        for actor in self.actors.all():
            actor = actor.to_dict()
            production['actors'].append(actor)
        for language in self.languages.all():
            language = language.to_dict()
            production['languages'].append(language)
        reviews = Review.objects.filter(production=self.id)
        for review in reviews:
            review = review.to_dict()
            production['reviews'].append(review)

        return production


class Review(models.Model):
    production = models.ForeignKey('Production', on_delete=models.CASCADE)
    source = models.CharField(max_length=48)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    possible = models.IntegerField()
    def __str__(self):
        return f'{self.production}: {self.source} - {self.score}/{self.possible}'
    def to_dict(self):
        return model_to_dict(self)