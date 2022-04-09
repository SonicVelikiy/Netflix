from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime
from .models import Movie, Actor, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, date):
        val_date = datetime.date(1950, 1, 1)
        if date < val_date:
            raise ValidationError(detail="Katta bo'lishi kerak")
        return date

class CommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Comment
        fields = ("id", "movie", "text", "created_date")