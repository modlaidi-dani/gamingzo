from django.urls import path,include
from rest_framework import routers
from . import views
from .views import *
router= routers.DefaultRouter()
router.register("contact", Contacte)

urlpatterns = [
    #product endoint: localhos/api/getProducts
    path('getProducts', Produit.as_view()),
    path('',include(router.urls)),
    path('affiliation',Affiliation.as_view()),
    #for checkout localhoste/api/checkout
    path('checkout',Chckout.as_view()),

]