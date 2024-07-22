from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.http import JsonResponse
from django.db.models import Prefetch, Q, Case, When, Count
from django.core.cache import cache
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
class Affiliation(viewsets.ModelViewSet):
    queryset=Affiliation.objects.all()
    serializer_class=AffiliationsSerializer
class Chckout(viewsets.ModelViewSet):
    queryset=CheckoutInfo.objects.all()
    serializer_class=CheckouSerializer
class NewsletterVienw(viewsets.ModelViewSet):
    queryset=Newsletter.objects.all()
    serializer_class=NewsletterSerializer
class Produit(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductrSerializer
    def list(self, request, *args, **kwargs):
        key="product_liste"
        products_data=cache.get(key)     
        if products_data is None:
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
                cache.set(key,products_data,timeout=15*60)  #15 MN 
        return  Response ({'products': products_data},status=status.HTTP_200_OK)
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        key = f"product_{pk}"
        product_data = cache.get(key)
        if product_data is None:        
            product = self.get_object()
            product_data = {
                "id": product.id,
                "name": product.designation,
                "description": product.description,
                "price": product.price,
                "images": product.get_image(),
                "stock": product.quantity,
                "deal": product.promo,
                "deal price": product.price_promo,
                "category": product.category.component if product.category else '',
                "filter": product.get_filters(),
                "config": product.config,
                "new": product.new,
                "sections": product.get_sections()
            }
            
            cache.set(key, product_data, timeout=15*60)  # 15 MN
        
        return Response({'product': product_data}, status=status.HTTP_200_OK)    

class HomeSection(viewsets.ModelViewSet):
    queryset=SectionHome.objects.all()
    serializer_class=SectionHomeSerializer
    def list(self, request, *args, **kwargs):
        sections = self.get_queryset()
        sections_data = []
        for section in sections:
            sections_data.append({
                "id": section.id,
                "title": section.title,
                "description": section.description,
                "image_url": section.image.get_rendition('fill-500x500').url if section.image else None,
                "link": section.link
            })  
        return  Response ( sections_data,status=status.HTTP_200_OK)
