from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
class Title(models.Model):
    title = models.CharField(max_length=50)
    
class SpotInfo(models.Model):
    location_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.CharField(max_length=200)
    appeal = models.CharField(max_length=500)
    good = models.IntegerField(default=0)
    visit = models.IntegerField(default=0)
    
class AppUser(models.Model):
    point = models.IntegerField(default=0)
    titles = models.ManyToManyField(Title, blank=True)
    ranking = models.IntegerField(default=0)
    
