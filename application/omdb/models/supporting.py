from django.db import models
from django.forms.models import model_to_dict


class Medium(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name
    def to_dict(self):
        return model_to_dict(self)

class Genre(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name
    def to_dict(self):
        return model_to_dict(self)

class Audience(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=48)
    description = models.TextField()

    def __str__(self):
        return self.code
    def to_dict(self):
        return model_to_dict(self)

class Director(models.Model):
    first = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)

    def __str__(self):
        return f'{self.first} {self.last}'
    def to_dict(self):
        return model_to_dict(self)

class Writer(models.Model):
    first = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)

    def __str__(self):
        return f'{self.first} {self.last}'
    def to_dict(self):
        return model_to_dict(self)

class Actor(models.Model):
    first = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)
    def __str__(self):
        return f'{self.first} {self.last}'
    def to_dict(self):
        return model_to_dict(self)

class Language(models.Model):
    name = models.CharField(max_length=48)
    abr =models.CharField(max_length=3)
    def __str__(self):
        return self.name
    def to_dict(self):
        return model_to_dict(self)