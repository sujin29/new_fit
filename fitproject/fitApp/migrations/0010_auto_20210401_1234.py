# Generated by Django 3.1.2 on 2021-04-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitApp', '0009_auto_20201020_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exer_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='nickname',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]