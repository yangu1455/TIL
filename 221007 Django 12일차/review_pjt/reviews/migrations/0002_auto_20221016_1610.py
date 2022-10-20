# Generated by Django 3.2.13 on 2022-10-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.FloatField(default=0.0),
        ),
    ]
