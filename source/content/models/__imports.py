from django.db.models import Model, CharField, TextField, ManyToManyField, AutoField, DateField, IntegerField, URLField, DateTimeField, JSONField, ForeignKey, DecimalField, CASCADE
from django.forms.models import model_to_dict
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action