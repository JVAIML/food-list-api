from django.db import models

class FoodRecipe(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    ingredients = models.JSONField()
    method = models.JSONField()
    values = {"veg":"veg", "non-veg":"non-veg"}
    category = models.CharField(choices=values, default="veg", max_length=255)
    recipe_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name