from django.urls import path
from .views import movieAPIView,actorAPIView

urlpatterns =[
    path('movie/', movieAPIView.as_view(), name = 'movie'),
    path('actor/', actorAPIView.as_view(), name = 'actor')
]