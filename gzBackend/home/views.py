import json
from django.shortcuts import render
from django import forms
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wagtail.models import Site
import logging
from maintenance_mode.core import get_maintenance_mode, set_maintenance_mode

ACTIVE_CHOICES = (
    (True, "Active"),
    (False, "Inactive"),
)

class MaintenanceForm(forms.Form):
    status = forms.ChoiceField(choices=ACTIVE_CHOICES)

logger = logging.getLogger(__name__)
def maintenance_toggle(request):
    print('the method is called')
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status'] == "True"  # Convert string to boolean
            set_maintenance_mode(status)
            
    
    context = {"form": MaintenanceForm(initial={'status': str(get_maintenance_mode())})}
    return render(request, 'wagtailmaintenance/maintenance-set.html', context)