# Generated by Django 4.1.3 on 2022-11-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotinfo',
            name='position_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spotinfo',
            name='position_y',
            field=models.IntegerField(default=0),
        ),
    ]
