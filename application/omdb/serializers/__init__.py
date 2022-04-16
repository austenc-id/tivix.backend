from rest_framework import serializers
from omdb.models import *


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['url', 'title', 'id']


class MediumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medium
        fields = ['url']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['url']


class AudienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audience
        fields = ['url']


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['url']


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ['url']


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['url']


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['url']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['url']