from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie,Actor


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
    # def validate_birthday(self,date):
    #     val_date = '1950.01.01'
    #     if date > val_date:
    #         raise ValidationError(detail="Katta bo'lishi kerak")
    #     return date