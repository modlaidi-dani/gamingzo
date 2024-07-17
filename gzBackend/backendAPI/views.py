from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from django.http import JsonResponse
from django.db.models import Prefetch, Q, Case, When, Count

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Category,ContactForm,Affiliation

from rest_framework import viewsets,generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class Contacte(viewsets.ModelViewSet):
    queryset=ContactForm.objects.all()
    serializer_class=ContacteSerializer
    def update(self, request, *args, **kwargs):
        return Response ({"ERROR": "Pas possible " }, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, *args, **kwargs):
        return Response ({"ERROR": "Pas possible " },status=status.HTTP_404_NOT_FOUND)
    def partial_update(self, request, *args, **kwargs):
        return Response ({"ERROR": "Pas possible " },status=status.HTTP_404_NOT_FOUND)
class Affiliation(generics.CreateAPIView):
    queryset=Affiliation.objects.all()
    serializer_class=AffiliationsSerializer

@csrf_exempt
def getHomeData(request):
    if request.method == 'GET':
        # print('request received')    
        products = models.Product.objects.all()  # Fetch all sections
        products_data = []
        for prod in products:
            products_data.append({
                "id": prod.id,
                "name": prod.designation,
                "description": prod.description,
                "price": prod.price,
                "images": prod.get_image(),
                "stock": prod.quantity,
                "deal": prod.promo,
                "deal price": prod.price_promo,
                "category": prod.category.component if prod.category else '',
                "filter": prod.get_filters(),
                "config": prod.config,
                "new": prod.new,
                "sections": prod.get_sections()
            }) 
        # print(products_data)    
        return JsonResponse({'products': products_data})    
    else: 
        return JsonResponse({'error': 'Method not allowed'}, status=405)
