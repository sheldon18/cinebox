from django.test import TestCase
from .models import Movie

# Create your tests here.
class MovieTest(TestCase):
    """The tests that will run against Movie models"""
    
    def test_str(self):
        test_name = Movie(name='A Movie')
        self.assertEqual(str(test_name), 'A Movie')