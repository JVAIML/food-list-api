from django.shortcuts import render
from rest_framework.views import APIView
from .models import foodlist
from django.http import JsonResponse
# Create your views here.

class food_list_view(APIView):
    def get(self,request):
        allfood = list(foodlist.objects.all().values())
        return JsonResponse(allfood, safe=False)