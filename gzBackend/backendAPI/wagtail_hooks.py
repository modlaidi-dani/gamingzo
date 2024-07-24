from wagtail import hooks
from django.urls import path
from .views import CheckoutInfoInspectView
from .admin import CheckoutInfoAdmin

@hooks.register('register_admin_urls')
def register_admin_urls():
  return [
    path('checkoutinfo/<int:instance_pk>/inspect/', 
         CheckoutInfoInspectView, 
         name='checkoutinfo_inspect'),
  ]