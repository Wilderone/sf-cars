# Generated by Django 3.0.8 on 2020-08-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]