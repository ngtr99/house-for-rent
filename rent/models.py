from django.db import models
from django.utils.text import slugify

class Account(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20) 
    status = models.CharField(
        max_length=10,
        choices=[
            ('Owner', 'Owner'),
            ('Tenant', 'Tenant'),
        ],
        default='Tenant',
    )
    def __str__(self):
        return self.username


# House Model
class House(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    location = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
