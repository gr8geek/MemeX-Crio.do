from django.db import models

# Create your models here.
class MyModel(models.Model):
    owner = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)
    url = models.URLField()
    
