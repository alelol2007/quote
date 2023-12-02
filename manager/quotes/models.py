from django.db import models

# Create your models here.
class info(models.Model):
    person = models.CharField(max_length= 200)
    quote = models.CharField(max_length= 200)