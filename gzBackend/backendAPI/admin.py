from django.urls import reverse
from django.utils.html import format_html
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import CheckoutInfo, ContactForm
from wagtail.contrib.modeladmin.views import InspectView

class CheckoutInfoInspectView(InspectView):
    def get_template_names(self):
        return ['wagtailadmin/pages/index.html']

class CheckoutInfoAdmin(ModelAdmin):
    model = CheckoutInfo
    menu_label = 'Checkout Orders'
    menu_icon = 'list-ul'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    inspect_view_class = CheckoutInfoInspectView  # Use custom inspect view
    list_display = ('first_name', 'last_name', 'wilaya', 'phone_num', 'email', 'inspect_link')
    list_export = ('first_name', 'last_name', 'wilaya', 'phone_num', 'email')
    list_filter = ('wilaya', )
    search_fields = ('email', 'first_name', )
    
    def inspect_link(self, obj):
        url = reverse('checkoutinfo_inspect', args=[obj.pk])
        return format_html('<a href="{}">Inspect</a>', url)

    inspect_link.short_description = 'Inspect'

modeladmin_register(CheckoutInfoAdmin)
    
class ContactFormAdmin(ModelAdmin):
    model = ContactForm
    menu_label = 'Contact Forms'
    menu_icon = 'mail'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    inspect_view_class = CheckoutInfoInspectView  # Use custom inspect view
    list_display = ('name', 'date', 'phoneNumber', 'company', 'email', 'Message')
    search_fields = ('name', 'date', 'phoneNumber', 'company', 'email')


modeladmin_register(ContactFormAdmin)
