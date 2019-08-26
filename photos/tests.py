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


class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new postor and saving it
        self.james= Postor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_postor()

        # Creating a new tag and saving it
        self.new_location = location(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',postor = self.james)
        self.new_image.save()

        self.new_image.location.add(self.new_tag)

    def tearDown(self):
        Postor.objects.all().delete()
        location.objects.all().delete()
        image.objects.all().delete()

    def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Image.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)