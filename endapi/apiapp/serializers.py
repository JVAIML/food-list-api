from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = '__all__'

    def validate(self, attrs):
        # Ensure all fields are not blank
        for field, value in attrs.items():
            if not value:
                raise serializers.ValidationError(f"{field.capitalize()} cannot be blank")
        return attrs