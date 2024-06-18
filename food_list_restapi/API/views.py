from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import foodlist
# Create your views here.

class food_list_view(APIView):
    def get(self,request):
        allfood = foodlist.object.all().values()
        return Response({"Message":"List of food","food list":allfood})

    def post(self,request):
        foodlist.object.create(id=request.data["id"],
                               food_name=request.data["food_name"],
                               food_type=request.data["food_type"],
                               recipe_type=request.data["recipe_type"],
                               recipe=request.data["recipe"])

        foodlist = foodlist.object.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New List of food","food list":foodlist})