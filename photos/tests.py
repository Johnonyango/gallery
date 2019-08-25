from django.test import TestCase
from .models import Postor,Image,tags


# Create your tests here.
class PostorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Postor(first_name = 'John', last_name ='Jonte', email ='j.yayah7@gmail.com')
