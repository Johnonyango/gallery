# Generated by Django 2.2.4 on 2019-08-26 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_image_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='category',
        ),
    ]
