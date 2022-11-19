from django.db import models

# Create your models here.
class sample(models.Model):
    hoge = models.CharField(max_length=10)
    piyo = models.CharField(max_length=10)