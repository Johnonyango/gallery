# Generated by Django 2.2.4 on 2019-08-27 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20190826_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]
