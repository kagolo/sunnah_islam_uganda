# Generated by Django 4.0.6 on 2022-08-09 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daawa', '0003_islam_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='islam_series',
            name='serie_lecture_video',
        ),
    ]
