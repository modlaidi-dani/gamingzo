# Generated by Django 4.2.14 on 2024-07-21 17:44

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0035_alter_product_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='state',
            field=models.CharField(choices=[('solved', 'Résolu'), ('en-attente', 'En Attente')], default='en-attente', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('fan size', 'Fan Size - Power Supply'), ('chipset', 'Chipset - CPU'), ('noise level', 'Noise Level - Cooler'), ('capacity', 'Capacity - RAM'), ('cores', 'Cores - CPU'), ('certifications', 'Certifications - Power Supply'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('sata ports', 'SATA Ports - Motherboard'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('eco_mode', 'Eco Mode - Power Supply'), ('form factor', 'Form Factor - Storage'), ('powerConsumption', 'Power Consumption - Cooler'), ('support', 'Support - Motherboard'), ('ports', 'Ports - GPU'), ('threads', 'Threads - CPU'), ('max memory', 'Max Memory - Motherboard'), ('pcie slots', 'PCIe Slots - Motherboard'), ('front panel ports', 'Front Panel Ports - Case'), ('motherboard support', 'Motherboard Support - Case'), ('dimensions', 'Dimensions - Power Supply'), ('refresh rate', 'Refresh Rate - Monitor'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('fan size', 'Fan Size - Cooler'), ('length', 'Length - GPU'), ('chipset', 'Chipset - GPU'), ('directx support', 'DirectX Support - GPU'), ('memory size', 'Memory Size - GPU'), ('radiator_size', 'Radiator Size - Cooler'), ('heat spreader', 'Heat Spreader - RAM'), ('wifi', 'WiFi - Motherboard'), ('memory interface', 'Memory Interface - GPU'), ('wattage', 'Wattage - Power Supply'), ('stream_processors', 'Stream Processors - GPU'), ('powerConsumption', 'Power Consumption - CPU'), ('architecture', 'Architecture - CPU'), ('type', 'Type - Storage'), ('read speed', 'Read Speed - Storage'), ('dimensions', 'Dimensions - Case'), ('panel type', 'Panel Type - Monitor'), ('usb ports', 'USB Ports - Motherboard'), ('modules', 'Modules - RAM'), ('airflow', 'Airflow - Cooler'), ('socket', 'Socket - CPU'), ('type', 'Type - Motherboard'), ('memory slots', 'Memory Slots - Motherboard'), ('latency', 'Latency - RAM'), ('size', 'Size - Monitor'), ('modularity', 'Modularity - Power Supply'), ('max gpu length', 'Max GPU Length - Case'), ('form factor', 'Form Factor - Case'), ('rgb', 'RGB - RAM'), ('capacity', 'Capacity - Storage'), ('memory speed', 'Memory Speed - Motherboard'), ('max psu length', 'Max PSU Length - Case'), ('memory type', 'Memory Type - GPU'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('tdp', 'TDP - CPU'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('socket', 'Socket - Motherboard'), ('interface', 'Interface - Storage'), ('bearing type', 'Bearing Type - Cooler'), ('resolution', 'Resolution - Monitor'), ('controller', 'Controller - Storage'), ('dimensions', 'Dimensions - RAM'), ('warranty', 'Warranty - Power Supply'), ('write speed', 'Write Speed - Storage'), ('max cpu height', 'Max CPU Height - Case'), ('type', 'Type - Cooler'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('lan', 'LAN - Motherboard'), ('cooling support', 'Cooling Support - Case'), ('dimensions', 'Dimensions - Cooler'), ('chipset', 'Chipset - Motherboard'), ('form factor', 'Form Factor - Motherboard'), ('powerConsumption', 'Power Consumption - GPU'), ('response time', 'Response Time - Monitor'), ('cache', 'Cache - CPU'), ('fan', 'Fan - Power Supply'), ('expansion slots', 'Expansion Slots - Case'), ('form factor', 'Form Factor - Power Supply'), ('voltage', 'Voltage - RAM'), ('rgb', 'RGB - Cooler'), ('drive bays', 'Drive Bays - Case'), ('powerConsumption', 'Power Consumption - Motherboard'), ('cuda cores', 'CUDA Cores - GPU'), ('connectivity', 'Connectivity - Monitor'), ('type', 'Type - RAM'), ('speed', 'Speed - RAM'), ('aspect ratio', 'Aspect Ratio - Monitor')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
