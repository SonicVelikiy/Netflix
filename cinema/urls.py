from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet,MovieActorAPIView,CommentMovieAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),
    path('movies/<int:id>/comment/', CommentMovieAPIView.as_view()),
    path('auth/', obtain_auth_token)
]