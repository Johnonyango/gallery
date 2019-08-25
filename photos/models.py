from django.db import models
import datetime as dt

# Create your models here.
class Postor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    # location = models.ManyToManyField(location)



    def __str__(self):
        return self.first_name

class Location(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length =30)


class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', default='DEFAULT VALUE')
    name = models.CharField(max_length =60)
    description = models.TextField()
    postor = models.ForeignKey(Postor, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def photos_of_day(cls):
        today = dt.date.today()
        photos = cls.objects.filter(post_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return photos

    

    