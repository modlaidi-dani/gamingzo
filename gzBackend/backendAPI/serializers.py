from .models import *
from rest_framework import serializers

class ContacteSerializer(serializers.ModelSerializer):
    class Meta:
            model = ContactForm
            fields=("object","dateSend","phoneNumber","Message")
class AffiliationsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Affiliation
            fields="__all__"
            