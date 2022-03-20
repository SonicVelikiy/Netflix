import datetime
from django.db import models
from .actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    year = models.DateField(default=datetime.date.today())
    imdb = models.IntegerField()
    genre = models.CharField(max_length=200, blank=True, null=True, choices=Actor.CHOIES)
    actor = models.ManyToManyField(Actor)
