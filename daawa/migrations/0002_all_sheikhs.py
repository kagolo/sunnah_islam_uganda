# Generated by Django 4.0.6 on 2022-07-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daawa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_sheikhs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheikh_name', models.CharField(max_length=200)),
                ('lecture_name', models.CharField(max_length=300)),
                ('lecture_date', models.DateTimeField()),
                ('lecture_image', models.ImageField(upload_to='l_pic')),
                ('lecture_video', models.FileField(upload_to='l_video')),
            ],
        ),
    ]
