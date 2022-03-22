from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer,ActorSerializer
from .models.movie import Movie,Actor

class movieAPIView(APIView):
    def get(self,request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)


class actorAPIView(APIView):
    def get(self,request):
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)
        return Response(data=serializer.data)
    def post(self,request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)