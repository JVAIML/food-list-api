from django.db import models

# Create your models here.

class foodlist(models.Model):
    id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=200)
    recipe= models.CharField(max_length=1000)
    food_type = models.CharField(max_length=200)
    recipe_type = models.CharField(max_length=200)