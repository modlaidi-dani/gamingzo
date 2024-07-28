from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.http import JsonResponse
from django.db.models import Prefetch, Q, Case, When, Count
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound

from rest_framework import viewsets,generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from wagtail.contrib.modeladmin.views import InstanceSpecificView
from .admin import CheckoutInfoAdmin

def CheckoutInfoInspectView(request, instance_pk):
    instance_pk = instance_pk
    checkout_object = CheckoutInfo.objects.get(id = instance_pk)
    checkout_products = ProductsInCheckout.objects.filter(checkout = checkout_object)
    context = {'checkout_info': checkout_object, 'checkout_products': checkout_products}
    return render(request, 'checkoutinfo_inspect.html', context)

class Contacte(viewsets.ModelViewSet):
    queryset=ContactForm.objects.all()
    serializer_class=ContacteSerializer
    
class Affiliation(viewsets.ModelViewSet):
    queryset=Affiliation.objects.all()
    serializer_class=AffiliationsSerializer
    
class Brands(viewsets.ModelViewSet):
    queryset=Brands.objects.all()
    serializer_class=BrandsSerializer
    def list(self, request, *args, **kwargs):
        brands = self.get_queryset()
        brands_data = []
        for brand in brands:
            brands_data.append({
                "key": brand.id,
                "name": brand.brand_name,
                "logo": brand.logo.file.url if brand.logo else None,
            })  
        return  Response (brands_data, status=status.HTTP_200_OK)
    
class Partners(viewsets.ModelViewSet):
    queryset=Partners.objects.all()
    serializer_class=PartnersSerializer
    def list(self, request, *args, **kwargs):
        partners = self.get_queryset()
        partners_data = []
        for partner in partners:
            partners_data.append({
                "id": partner.id,
                "name": partner.partner_name,
                "phone": partner.phone,
                "adress": partner.adress,
                "logo": partner.logo.file.url if partner.logo else None,
            })  
        return  Response ( partners_data,status=status.HTTP_200_OK)
    
class FAQ(viewsets.ModelViewSet):
    queryset=FAQ.objects.all()
    serializer_class=FAQSerializer

class checkoutProduct(viewsets.ModelViewSet):
    queryset=ProductsInCheckout.objects.all()
    serializer_class=ProductCheckoutserialiser

class Chckout(viewsets.ModelViewSet):
    queryset=CheckoutInfo.objects.all()
    serializer_class=CheckouSerializer
    def create(self, request, *args, **kwargs):
        data=request.data
        products = data.product
        productsafter=[]
        for product in len(products):
            product =checkoutProduct.obejects.creat(product)
            productsafter.append(product)
        serializer=self.get_serializer(data=data)
        if serializer.is_valid():
            data=serializer.save()
            for product in productsafter:
                product.checkout=data
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class NewsletterVienw(viewsets.ModelViewSet):
    queryset=Newsletter.objects.all()
    serializer_class=NewsletterSerializer
    
class Produit(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductrSerializer
    def list(self, request, *args, **kwargs):
        key="product_liste"
        products_data=cache.get(key)     
        if products_data:
            print("i am using the cache")
            return  Response ({'products': products_data, "source " :'cache '},status=status.HTTP_200_OK)

        elif products_data is None  :
            products = self.get_queryset()
            products_data = []
            for prod in products:
                products_data.append({
                    "id": prod.id,
                    "name": prod.designation,
                    "description": prod.description,
                    "header_description": prod.header_description,
                    "price": prod.price,
                    "images": prod.get_image(),
                    "stock": prod.quantity,
                    "deal": prod.promo,
                    "deal price": prod.price_promo,
                    "category": prod.category.component if prod.category else '',
                    "filter": prod.get_filters(),
                    "config": prod.config,
                    "new": prod.new,
                    "specifications": prod.get_specs(),
                    "sections": prod.get_sections()
                })
                print(prod.get_specs())
                cache.set(key,products_data,timeout=15*60)  #15 MN 
        return  Response ({'products': products_data, 'source': 'database'},status=status.HTTP_200_OK)
    
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
                "header_description": product.header_description,
                "price": product.price,
                "images": product.get_image(),
                "stock": product.quantity,
                "deal": product.promo,
                "deal price": product.price_promo,
                "category": product.category.component if product.category else '',
                "filter": product.get_filters(),
                "config": product.config,
                "new": product.new,
                "specifications": product.get_specs(),
                "sections": product.get_sections()
            }
            print(product.get_specs())
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
    
class Event(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventsSerializer
    def list(self, request, *args, **kwargs):
        events = self.get_queryset()
        events_data = []
        for event in events:
            events_data.append({
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "date": event.date,
                "promo_text": event.promo_text,
                "image": event.image.file.url if event.image else None,
                "gallery": event.getGallery()
            })  
        return  Response ( events_data,status=status.HTTP_200_OK)


