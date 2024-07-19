from .models import *
from rest_framework import serializers

class ContacteSerializer(serializers.ModelSerializer):
    class Meta:
            model = ContactForm
            fields=("name","company","email","phoneNumber","Message")
class AffiliationsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Affiliation
            fields="__all__"
class ProductrSerializer(serializers.ModelSerializer):
    class Meta:
            model = Product
            fields="__all__"
class CheckouSerializer(serializers.ModelSerializer):
    class Meta:
            model = CheckoutInfo
            fields="__all__"
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
            model = Newsletter
            fields="__all__"
