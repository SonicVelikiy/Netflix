from django.db import models

class Actor(models.Model):
    male = "Male"
    female = "Female"
    CHOIES = (
        (male,"Male"),
        (female,"Female"),
    )
    name = models.CharField(max_length=200,blank=False,null=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=200,blank=False,null=False,choices=CHOIES)