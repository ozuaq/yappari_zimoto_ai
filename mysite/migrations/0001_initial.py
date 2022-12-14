# Generated by Django 4.1.3 on 2022-11-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SpotInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('appeal', models.CharField(max_length=500)),
                ('good', models.IntegerField(default=0)),
                ('visit', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(blank=True, to='mysite.tag')),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=0)),
                ('titles', models.ManyToManyField(blank=True, to='mysite.title')),
            ],
        ),
    ]
