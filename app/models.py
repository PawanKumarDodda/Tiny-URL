from django.db import models

# Create your models here.
class Short(models.Model):
    url=models.CharField(max_length=100)
    shortcode=models.CharField(max_length=100)
