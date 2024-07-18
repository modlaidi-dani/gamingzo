from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.http import JsonResponse
from django.db.models import Prefetch, Q, Case, When, Count

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Category,ContactForm,Affiliation

from rest_framework import viewsets,generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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
class Chckout(generics.CreateAPIView):
    queryset=CheckoutInfo.objects.all()
    serializer_class=CheckouSerializer
class Produit(generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductrSerializer
    def list(self, request, *args, **kwargs):
        products = self.get_queryset()
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
        return  Response ({'products': products_data},status=status.HTTP_200_OK)
    



