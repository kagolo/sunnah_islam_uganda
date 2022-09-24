from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.deletion import CASCADE

# Create your models here.



class Favorite_sheikhs(models.Model):
    sheikh_name=models.CharField(max_length=200,null=False)
    lecture_name=models.CharField(max_length=300,null=False)
    lecture_date=models.DateTimeField()
    lecture_image=models.ImageField(upload_to='l_pic')
    lecture_video=models.FileField(upload_to='l_video')

class All_sheikhs(models.Model):
    sheikh_name=models.CharField(max_length=200,null=False)
    lecture_name=models.CharField(max_length=300,null=False)
    lecture_date=models.DateTimeField()
    lecture_image=models.ImageField(upload_to='l_pic')
    lecture_video=models.FileField(upload_to='l_video')

class Islam_series(models.Model):
    sheikh_name=models.CharField(max_length=200,null=False)
    serie_lecture_name=models.CharField(max_length=300,null=False)
    serie_lecture_date=models.DateTimeField()
    serie_lecture_image=models.ImageField(upload_to='l_pic')

class Islam_serie_episode(models.Model):
    islam_serie=models.ForeignKey(Islam_series,on_delete=CASCADE)
    sheikh_name=models.CharField(max_length=200,null=False)
    episode_lecture_name=models.CharField(max_length=300,null=False)
    episode_lecture_date=models.DateTimeField()
    episode_lecture_image=models.ImageField(upload_to='l_pic')
    episode_lecture_video=models.FileField(upload_to='l_video')

    

