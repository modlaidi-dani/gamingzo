from django.urls import path, reverse
from django.urls import path

from wagtail.admin.menu import MenuItem
from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from .views import maintenance_toggle
@hooks.register('register_admin_urls')
def register_maintenance_url():
    return [
        path('maintenance-set/', maintenance_toggle, name='maintenance_toggle'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    return MenuItem('Maintenance', reverse('maintenance_toggle'), icon_name='chain-broken')
