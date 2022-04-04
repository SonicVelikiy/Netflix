from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer,ActorSerializer,CommentSerializer
from .models import Movie,Actor,Comment



class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    @action(detail=True,methods=["POST"],url_path='add_actor/(?P<id>\d+)')
    def add_actor(self, request, id, *args, **kwargs):
        movie = self.get_object()
        movie.actor.add(id)
        movie.save()
        return Response(status=status.HTTP_200_OK)
        #http://127.0.0.1:8000/movies/movie_id/add_actor/actor_id/

    @action(detail=True, methods=["POST"], url_path='remove_actor/(?P<id>\d+)')
    def remove_actor(self, request, id, *args, **kwargs):
        movie = self.get_object()
        movie.actor.remove(id)
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # http://127.0.0.1:8000/movies/movie_id/add_actor/remove_actor_id/

    @action(detail=True, methods=["GET"])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actor.all(), many=True)
        return Response(data=serializer.data)
        # http://127.0.0.1:8000/movies/<int:id>/actors/

class MovieActorAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def actions(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actor.all(), many=True)
        return Response(serializer.data)

class CommentMovieAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        data = Movie.objects.filter(id=self.kwargs['id'])
        # serdata = MovieSerializer(data, many=False)
        serializer.save(movie= data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer