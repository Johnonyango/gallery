# Generated by Django 2.2.4 on 2019-08-25 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20190825_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post_date',
        ),
    ]
