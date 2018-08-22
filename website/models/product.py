from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    '''
    author: Joe Shep
    edited: added category, date_added, rating, like, and location.
    purpose: create product object
    '''
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)
    date_added = models.DateField(auto_now=False, auto_now_add=False)
    rating = models.IntegerField(
           default=1,
           validators=[MaxValueValidator(5), MinValueValidator(1)])
    like = models.BooleanField(default=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title