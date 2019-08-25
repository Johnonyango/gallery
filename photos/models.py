from django.db import models

# Create your models here.
class Postor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
    tags = models.ManyToManyField(tags)

    