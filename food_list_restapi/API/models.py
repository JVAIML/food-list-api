from django.db import models

# Create your models here.

class foodlist(models.Model):
    id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=200)
    recipe = models.CharField(max_length=1000)
    food_type_values = {"veg":"veg", "non-veg":"non-veg"}
    food_type = models.CharField(max_length=7, choices=food_type_values, default="veg")
    recipe_type = models.CharField(max_length=200)