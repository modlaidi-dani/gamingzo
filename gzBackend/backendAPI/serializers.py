from .models import *
from rest_framework import serializers

class ContacteSerializer(serializers.ModelSerializer):
    class Meta:
            model = ContactForm
            fields=("name","company","email","phoneNumber","Message")
            
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Event
            fields="__all__"
            
class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Brands
            fields="__all__"
            
class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
            model = Partners
            fields="__all__"
            
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
            model = FAQ
            fields="__all__"
            
class AffiliationsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Affiliation
            fields="__all__"
            
class ProductrSerializer(serializers.ModelSerializer):
    class Meta:
            model = Product
            fields="__all__"

class ProductCheckoutserialiser(serializers.ModelSerializer):
    class Meta:
            model= ProductsInCheckout
            fields="__all__"

class CheckouSerializer(serializers.ModelSerializer):
    product=ProductCheckoutserialiser(many=True)
    class Meta:
            model = CheckoutInfo
            fields="__all__"
    def validate(self, data):
          product=data.get('product')
          if len(product)==0:
             raise serializers.ValidationError('put a product')
          return super().validate(data) 

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
            model = Newsletter
            fields="__all__"

class SectionHomeSerializer(serializers.ModelSerializer):
    class Meta:
            model = SectionHome
            fields="__all__"