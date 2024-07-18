# Generated by Django 4.2.14 on 2024-07-18 12:24

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0017_alter_contactform_state_alter_product_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='state',
            field=models.CharField(choices=[('en-attente', 'En Attente'), ('solved', 'Résolu')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('type', 'Type - Cooler'), ('chipset', 'Chipset - Motherboard'), ('powerConsumption', 'Power Consumption - Cooler'), ('fan size', 'Fan Size - Cooler'), ('max psu length', 'Max PSU Length - Case'), ('cache', 'Cache - CPU'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('connectivity', 'Connectivity - Monitor'), ('rgb', 'RGB - RAM'), ('threads', 'Threads - CPU'), ('response time', 'Response Time - Monitor'), ('modules', 'Modules - RAM'), ('form factor', 'Form Factor - Storage'), ('capacity', 'Capacity - Storage'), ('dimensions', 'Dimensions - Case'), ('rgb', 'RGB - Cooler'), ('memory speed', 'Memory Speed - Motherboard'), ('lan', 'LAN - Motherboard'), ('latency', 'Latency - RAM'), ('form factor', 'Form Factor - Motherboard'), ('fan size', 'Fan Size - Power Supply'), ('resolution', 'Resolution - Monitor'), ('chipset', 'Chipset - CPU'), ('powerConsumption', 'Power Consumption - Motherboard'), ('size', 'Size - Monitor'), ('socket', 'Socket - Motherboard'), ('cooling support', 'Cooling Support - Case'), ('airflow', 'Airflow - Cooler'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('eco_mode', 'Eco Mode - Power Supply'), ('powerConsumption', 'Power Consumption - GPU'), ('memory slots', 'Memory Slots - Motherboard'), ('usb ports', 'USB Ports - Motherboard'), ('pcie slots', 'PCIe Slots - Motherboard'), ('bearing type', 'Bearing Type - Cooler'), ('type', 'Type - RAM'), ('write speed', 'Write Speed - Storage'), ('length', 'Length - GPU'), ('wattage', 'Wattage - Power Supply'), ('warranty', 'Warranty - Power Supply'), ('panel type', 'Panel Type - Monitor'), ('memory size', 'Memory Size - GPU'), ('controller', 'Controller - Storage'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('speed', 'Speed - RAM'), ('interface', 'Interface - Storage'), ('architecture', 'Architecture - CPU'), ('read speed', 'Read Speed - Storage'), ('cuda cores', 'CUDA Cores - GPU'), ('modularity', 'Modularity - Power Supply'), ('tdp', 'TDP - CPU'), ('form factor', 'Form Factor - Case'), ('expansion slots', 'Expansion Slots - Case'), ('socket', 'Socket - CPU'), ('ports', 'Ports - GPU'), ('form factor', 'Form Factor - Power Supply'), ('support', 'Support - Motherboard'), ('max memory', 'Max Memory - Motherboard'), ('max cpu height', 'Max CPU Height - Case'), ('voltage', 'Voltage - RAM'), ('noise level', 'Noise Level - Cooler'), ('dimensions', 'Dimensions - RAM'), ('capacity', 'Capacity - RAM'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('dimensions', 'Dimensions - Cooler'), ('drive bays', 'Drive Bays - Case'), ('heat spreader', 'Heat Spreader - RAM'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('radiator_size', 'Radiator Size - Cooler'), ('wifi', 'WiFi - Motherboard'), ('fan', 'Fan - Power Supply'), ('stream_processors', 'Stream Processors - GPU'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('certifications', 'Certifications - Power Supply'), ('max gpu length', 'Max GPU Length - Case'), ('chipset', 'Chipset - GPU'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('memory type', 'Memory Type - GPU'), ('cores', 'Cores - CPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('motherboard support', 'Motherboard Support - Case'), ('type', 'Type - Motherboard'), ('dimensions', 'Dimensions - Power Supply'), ('directx support', 'DirectX Support - GPU'), ('type', 'Type - Storage'), ('front panel ports', 'Front Panel Ports - Case'), ('memory interface', 'Memory Interface - GPU'), ('powerConsumption', 'Power Consumption - CPU'), ('sata ports', 'SATA Ports - Motherboard')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
