from rest_framework import serializers
from omdb.models import *


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['url', 'id', 'title', 'year', 'poster']


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['url']