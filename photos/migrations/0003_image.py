# Generated by Django 2.2.4 on 2019-08-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
    ]