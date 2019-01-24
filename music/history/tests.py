import unittest
from django.test import TestCase
from django.urls import reverse

from .models import Artist
# Create your tests here.

# stuff to test
  # context: what we send to the template
  # content: the rendered html
  # response_codes

# name your tests like this: test_foo so Django can find and run them

# the test client is a Python class that acts as a dummy web browser, allowing you to test your views and interact with your Django - powered application programmatically. Some of the things you can do with the test client are:
  # simulate GET and POST requests on a URL and observer the response - everything from low - level HTTP(result headers and status codes) to page content.
  # see the chain of redirects if any and check the URL and staus code at each step
  # test that a given request....


class ArtistTest(TestCase):

    def test_list_artists(self):
      new_artist =  Artist.objects.create(
        name='',
      )

      # issue a GET request. client is a dummy web browser
      # reverse is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
      response = self.client.get(reverse('history:artists'))

      # check that the response is 200 ok
      self.assertEqual(response.status_code, 200)

      # check that rendered context contains one item
      self.assertEqual(len(response.context['artist_list']), 1)

      # .encode converts from unicode to utf-8
      self.assertIn(new_artist.name.encode(), response.content)

    # def test_get_artist_form(self):
    #   response = self.client.get(reverse('history:artist_form'))


      # test whether object value added to database matches what's returned
    # def test_get_artist_detail(self):
    #     new_artist = Artist.objects.create(
    #       name='Suzy Saxophone'
    #     )

    #     response = self.client.get(reverse('history:artist_detail', args=(1,)))
    #     self.assertEqual(response.context['artist_detail'].name, new_artist.name)