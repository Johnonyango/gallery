# Generated by Django 2.2.4 on 2019-08-26 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='title',
        ),
    ]