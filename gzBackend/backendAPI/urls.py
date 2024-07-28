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
router.register("getEvents", Event,basename="event")
router.register("getFAQ", FAQ,basename="faq")
router.register("getBrands", Brands,basename="brand")
router.register("getPartners", Partners,basename="partners")
router.register("SectionHome", HomeSection,basename="SectionHome")

urlpatterns = [
    path('',include(router.urls)),
    # path('/admin/admin/checkoutinfo/<int:instance_pk>/inspect/', 
    #      CheckoutInfoInspectView.as_view(model_admin=CheckoutInfoAdmin), 
    #      name='checkoutinfo_inspect'),
    #checkout: localhoste/api/checkout
    #product : localhos/api/getProducts
    #affiliation : localhos/api/affiliation
    #newsletter : localhos/api/newsletter
    #contact : localhos/api/contact
]