from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer
from django.http import JsonResponse

# Create your views here.

class FoodRecipePost(APIView):
    def get(self, request):
        allfood = FoodRecipe.objects.all().values()
        return Response(allfood)
    
    def post(self, request):
        serializer = FoodRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodRecipePatch(APIView):
    def get(self, request, id):
        food = FoodRecipe.objects.all().values().filter(id=id)
        return Response(food)
    
    def patch(self, request, id):
        model_object = FoodRecipe.objects.get(id=id)
        serializer = FoodRecipeSerializer(model_object, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("tet")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodRecipeView(APIView):
    def get(self, request, category):
        rtype = request.GET.get('recipe_type', '')
        serializer = FoodRecipeSerializer(data=request.data)
        if(rtype == ''):
            return JsonResponse({"status":"FAILED","comment":"recipe_type: Field should not be empty"}, safe=False)
        data = []
        if(category == "all"):
            if(rtype == "all"):
                data = list(FoodRecipe.objects.all().values())
            else:
                if(category == "nonveg"):
                    category = "non-veg"
                data = list(FoodRecipe.objects.all().filter(recipe_type=rtype).values())
        else:
            if(rtype == "all"):
                data = list(FoodRecipe.objects.all().filter(category=category).values())
            else:
                if(category == "nonveg"):
                    category = "non-veg"
                data = list(FoodRecipe.objects.all().filter(category=category, recipe_type=rtype).values())
        return JsonResponse(data, safe=False)