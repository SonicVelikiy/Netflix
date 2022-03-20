from django.db import models

class Actor(models.Model):
    action = "Action"
    comedy = "Comedy"
    drama = "Drama"
    fantasy = "Fantasy"
    romance = "Romance"
    thriller = "Thriller"
    CHOIES = (
        (action,"Action"),
        (comedy,"Comedy"),
        (drama,"Drama"),
        (fantasy,"Fantasy"),
        (romance,"Romance"),
        (thriller,"Thriller"),
    )
    name = models.CharField(max_length=200,blank=True,null=True)
    birthdate = models.DateField()
    gender = models.CharField(max_length=200,blank=False,null=False,choices=CHOIES)