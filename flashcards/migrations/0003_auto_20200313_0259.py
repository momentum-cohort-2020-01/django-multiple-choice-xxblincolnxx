# Generated by Django 3.0.4 on 2020-03-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_auto_20200310_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textcard',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
    ]
