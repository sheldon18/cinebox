from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, default='')
    release = models.CharField(max_length=4, default='')
    trailer = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        