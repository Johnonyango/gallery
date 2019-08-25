from django.test import TestCase
from .models import Postor,Image,Location


# Create your tests here.
class PostorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Postor(first_name = 'John', last_name ='Jonte', email ='j.yayah7@gmail.com')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.john,Postor))

    # Testing Save Method
    def test_save_method(self):
        self.john.save_postor()
        postors = Postor.objects.all()
        self.assertTrue(len(postors) > 0)