# Generated by Django 3.0.4 on 2020-03-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0010_auto_20200317_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='figure_raw',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]