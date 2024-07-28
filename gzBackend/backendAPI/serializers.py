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

class ProductCheckoutserialiser(serializers.ModelSerializer):
    class Meta:
            model= ProductsInCheckout
            fields="__all__"
      

class CheckouSerializer(serializers.ModelSerializer):
    product=ProductCheckoutserialiser(many=True)
    class Meta:
            model = CheckoutInfo
            fields="__all__"
    def to_internal_value(self, data):
          products=data.get('product')
        #  print(data)
          pt=[]
          for p in products:
                p={"product_id":p["id"],"unitprice":p["price"],"quantity":p["quantity"],"total":(p["price"]*p["quantity"]) }
                pt.append(p)
          data['product']=pt
          return data
    def create(self, validated_data):
        data_v=validated_data
        products_data = validated_data.get('product')
        checkou_data= validated_data.pop('product')
        checkout_instance = CheckoutInfo.objects.create(**validated_data)       
        for product_data in products_data:
            product=ProductsInCheckout.objects.create(checkout=checkout_instance, product=Product.objects.get(id=product_data["product_id"]),quantity=product_data["quantity"],unitprice=product_data["unitprice"])
           
        return data_v
            
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
            model = Newsletter
            fields="__all__"
            
class SectionHomeSerializer(serializers.ModelSerializer):
    class Meta:
            model = SectionHome
            fields="__all__"