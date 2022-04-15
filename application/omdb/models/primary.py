from django.db import models
from .supporting import Medium, Genre, MPA_Rating, Director, Writer, Actor, Language, Rating

class Production(models.Model):
    medium = models.ForeignKey(Medium, null=True, on_delete=models.SET_NULL, related_name='production_edium')
    title = models.CharField(max_length=48)
    date = models.DateField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='production_genres')
    audience = models.ForeignKey(MPA_Rating, null=True, on_delete=models.SET_NULL, related_name='production_audience')
    length = models.IntegerField()
    directors = models.ManyToManyField(Director, related_name='production_directors')
    writers = models.ManyToManyField(Writer, related_name='production_writers')
    actors = models.ManyToManyField(Actor, related_name='production_actors')
    languages = models.ManyToManyField(Language, related_name='production_languages')
    country = models.CharField(max_length=48)
    awards = models.TextField()
    poster = models.URLField()
    reviews = models.ManyToManyField(Rating, related_name='production_ratings')
    box_office = models.IntegerField()

    def year(self):
        return self.date.year

    def __str__(self):
        return self.title