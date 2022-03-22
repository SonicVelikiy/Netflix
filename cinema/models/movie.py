import datetime
from django.db import models
from .actor import Actor

class Movie(models.Model):
    action = "Action"
    comedy = "Comedy"
    drama = "Drama"
    fantasy = "Fantasy"
    romance = "Romance"
    thriller = "Thriller"
    CHOIES = (
        (action, "Action"),
        (comedy, "Comedy"),
        (drama, "Drama"),
        (fantasy, "Fantasy"),
        (romance, "Romance"),
        (thriller, "Thriller"),
    )
    name = models.CharField(max_length=200, blank=False, null=False)
    year = models.DateField()
    imdb = models.IntegerField()
    genre = models.CharField(max_length=200, blank=True, null=True, choices=CHOIES)
    actor = models.ManyToManyField(Actor)
