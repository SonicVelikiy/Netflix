import datetime
from django.db import models
# from .actor import Actor

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


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    year = models.DateField(default=datetime.date.today())
    imdb = models.URLField(blank=False, null=False)
    genre = models.CharField(max_length=200, blank=True, null=True, choices=CHOIES)
    # actor = models.ManyToManyField(Actor)
