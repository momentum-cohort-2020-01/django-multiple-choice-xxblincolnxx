# Generated by Django 3.0.4 on 2020-03-18 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0014_auto_20200318_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='cropping',
        ),
    ]