# Generated by Django 3.1.2 on 2020-10-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]