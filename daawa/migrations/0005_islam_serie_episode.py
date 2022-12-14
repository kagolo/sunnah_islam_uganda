# Generated by Django 4.0.6 on 2022-08-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daawa', '0004_remove_islam_series_serie_lecture_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Islam_serie_episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheikh_name', models.CharField(max_length=200)),
                ('episode_lecture_name', models.CharField(max_length=300)),
                ('episode_lecture_date', models.DateTimeField()),
                ('episode_lecture_image', models.ImageField(upload_to='l_pic')),
                ('episode_lecture_video', models.FileField(upload_to='l_video')),
            ],
        ),
    ]
