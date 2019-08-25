from django.db import models
import datetime as dt

# Create your models here.
class Postor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name

class Location(models.Model):
    name = models.CharField(max_length =30)


    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    postor = models.ForeignKey(Postor, on_delete='SOME STRING')
    post_date = models.DateTimeField(auto_now_add=True)

    

    