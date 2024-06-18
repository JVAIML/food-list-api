from django.shortcuts import render
from rest_framework.views import APIView
from .models import foodlist
from django.http import JsonResponse
# Create your views here.

class food_list_view(APIView):
    def get(self, request, food_type):
        rtype = request.GET.get('recipe_type', '')
        data = []
        if(food_type == "veg"):
            if(rtype == ""):
                data = list(foodlist.objects.all().filter(food_type="veg").values())
            else:
                data = list(foodlist.objects.all().filter(food_type="veg", recipe_type=rtype).values())
        elif(food_type == "nonveg"):
            if(rtype == ""):
                data = list(foodlist.objects.all().filter(food_type="non-veg").values())
            else:
                data = list(foodlist.objects.all().filter(food_type="non-veg", recipe_type=rtype).values())
        elif(food_type == "all"):
            if(rtype == ""):
                data = list(foodlist.objects.all().filter().values())
            else:
                data = list(foodlist.objects.all().filter(recipe_type=rtype).values())
        return JsonResponse(data, safe=False)
