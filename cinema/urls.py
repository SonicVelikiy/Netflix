from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet,MovieActorAPIView,CommentMovieAPIView,CommentMovieListAPIView,CommentMovieDestroyAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),
    path('movie/comment/', CommentMovieAPIView.as_view()),
    path('comments/', CommentMovieListAPIView.as_view()),
    path('comment/<int:pk>/', CommentMovieDestroyAPIView.as_view()),
    path('auth/', obtain_auth_token)
    ]