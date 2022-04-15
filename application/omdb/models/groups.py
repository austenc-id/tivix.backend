from django.db import models
from .supporting import Medium
class Gallery(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    title = models.CharField(max_length=48)
    description = models.TextField()
    productions = models.ManyToManyField('Production', null=True,related_name='gallery_productions')
