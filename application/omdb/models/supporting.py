from django.db import models


class Medium(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=48)
    def __str__(self):
        return self.name

class MPA_Rating(models.Model):
    class Meta:
        verbose_name = 'MPA_Rating'
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=48)
    description = models.TextField()
    def __str__(self):
        return self.code


class Director(models.Model):
    first = models.CharField(max_length=48, null=True)
    middle = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)
    def __str__(self):
        if self.middle is not None:
            return f'{self.first} {self.middle} {self.last}'
        else:
            return f'{self.first} {self.last}'


class Writer(models.Model):
    first = models.CharField(max_length=48, null=True)
    middle = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)
    def __str__(self):
        if self.middle is not None:
            return f'{self.first} {self.middle} {self.last}'
        else:
            return f'{self.first} {self.last}'


class Actor(models.Model):
    first = models.CharField(max_length=48, null=True)
    middle = models.CharField(max_length=48, null=True)
    last = models.CharField(max_length=48, null=True)
    def __str__(self):
        if self.middle is not None:
            return f'{self.first} {self.middle} {self.last}'
        else:
            return f'{self.first} {self.last}'


class Language(models.Model):
    name = models.CharField(max_length=48)
    abr =models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Rating(models.Model):
    source = models.CharField(max_length=48)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    possible = models.IntegerField()
    sample_size = models.IntegerField()
    def __str__(self):
        return f'{self.source} - {self.score}/{self.possible}'