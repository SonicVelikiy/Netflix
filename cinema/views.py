from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieSerializer,ActorSerializer
from .models.movie import Movie,Actor



class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    @action(detail=True,methods=["POST"],url_path='add_actor/(?P<id>\d+)')
    def add_actor(self, request, id, *args, **kwargs):
        movie = self.get_object()
        movie.actor.add(id)
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
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


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer










# class movieAPIView(APIView):
#     def get(self,request):
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie, many=True)
#         return Response(data=serializer.data)
#
#
# class actorAPIView(APIView):
#     def get(self,request):
#         actor = Actor.objects.all()
#         serializer = ActorSerializer(actor, many=True)
#         return Response(data=serializer.data)
#     def post(self,request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(data=serializer.data)