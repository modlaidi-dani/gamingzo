from django.urls import path,include
from rest_framework import routers
from . import views
from .views import *
router= routers.DefaultRouter()
router.register("contact", Contacte)

urlpatterns = [
    path('getProducts', views.getHomeData, name="prod-data"),
    path('',include(router.urls)),
    path('affiliation',Affiliation.as_view())
]