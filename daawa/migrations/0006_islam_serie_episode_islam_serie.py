# Generated by Django 4.0.6 on 2022-08-14 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daawa', '0005_islam_serie_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='islam_serie_episode',
            name='islam_serie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='daawa.islam_series'),
            preserve_default=False,
        ),
    ]
