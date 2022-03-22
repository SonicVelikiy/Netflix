from django.urls import path
from .views import movieAPIView,actorAPIView

urlpatterns =[
    path('movies/', movieAPIView.as_view(), name = 'movie'),
    path('actors/', actorAPIView.as_view(), name = 'actor')
]