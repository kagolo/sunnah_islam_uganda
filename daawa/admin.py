from django.contrib import admin
from django.db import models
from .models import Favorite_sheikhs, All_sheikhs, Islam_series, Islam_serie_episode

# Register your models here.


admin.site.register(Favorite_sheikhs)
admin.site.register(All_sheikhs)
admin.site.register(Islam_series)
admin.site.register(Islam_serie_episode)