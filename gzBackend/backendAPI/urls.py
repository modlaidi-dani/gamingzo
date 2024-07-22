from django.urls import path,include
from rest_framework import routers
from . import views
from .views import *
router= routers.DefaultRouter()
router.register("contact", Contacte,basename="contact")
router.register("checkout", Chckout,basename="checkout")
router.register("affiliation", Affiliation,basename="affiliation")
router.register("newsletter", NewsletterVienw,basename="newsletter")
router.register("getProducts", Produit,basename="product")
router.register("SectionHome", HomeSection,basename="SectionHome")
urlpatterns = [
    path('',include(router.urls))
    #checkout: localhoste/api/checkout
    #product : localhos/api/getProducts
    #affiliation : localhos/api/affiliation
    #newsletter : localhos/api/newsletter
    #contact : localhos/api/contact

]