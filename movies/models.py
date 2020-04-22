from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, default='')
    release = models.IntegerField()
    trailer = models.URLField(max_length=254, default='')
    price = models.DecimalField(max_digits=2, decimal_places=0)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        