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
    location_name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.location_name
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location):
        location = cls.objects.get(pk=id)
        location = cls(location=location)
        location.save()

    

class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,category):
        category = cls.objects.get(pk=id)
        category = cls(category=category)
        category.save()

    

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', default='DEFAULT VALUE')
    title = models.CharField(max_length =60)
    description = models.TextField()
    postor = models.ForeignKey(Postor, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    location_name = models.CharField(max_length =30, default='DEFAULT VALUE')


    
    @classmethod
    def photos_of_day(cls):
        today = dt.date.today()
        photos = cls.objects.filter(post_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return photos

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

    