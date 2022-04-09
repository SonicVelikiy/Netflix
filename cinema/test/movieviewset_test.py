from django.test import TestCase, Client

from Netflix.cinema.models import Movie


class MovieViewSetTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name="Test movie", year="10.02.2022", imdb="122", genre="Action", actor=[1])
        self.client = Client()

    def test_get_movie(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Test movie')
