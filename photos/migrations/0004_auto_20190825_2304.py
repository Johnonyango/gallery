# Generated by Django 2.2.4 on 2019-08-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/'),
        ),
    ]
