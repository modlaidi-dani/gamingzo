# Generated by Django 4.2.14 on 2024-07-22 13:05

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0049_alter_product_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='state',
            field=models.CharField(choices=[('en-attente', 'En Attente'), ('solved', 'Résolu')], default='en-attente', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('memory speed', 'Memory Speed - Motherboard'), ('type', 'Type - Motherboard'), ('write speed', 'Write Speed - Storage'), ('rgb', 'RGB - RAM'), ('capacity', 'Capacity - RAM'), ('architecture', 'Architecture - CPU'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('lan', 'LAN - Motherboard'), ('threads', 'Threads - CPU'), ('capacity', 'Capacity - Storage'), ('interface', 'Interface - Storage'), ('dimensions', 'Dimensions - RAM'), ('chipset', 'Chipset - CPU'), ('cores', 'Cores - CPU'), ('chipset', 'Chipset - Motherboard'), ('expansion slots', 'Expansion Slots - Case'), ('radiator_size', 'Radiator Size - Cooler'), ('warranty', 'Warranty - Power Supply'), ('powerConsumption', 'Power Consumption - Cooler'), ('directx support', 'DirectX Support - GPU'), ('eco_mode', 'Eco Mode - Power Supply'), ('fan size', 'Fan Size - Power Supply'), ('form factor', 'Form Factor - Power Supply'), ('panel type', 'Panel Type - Monitor'), ('drive bays', 'Drive Bays - Case'), ('pcie slots', 'PCIe Slots - Motherboard'), ('memory type', 'Memory Type - GPU'), ('rgb', 'RGB - Cooler'), ('max psu length', 'Max PSU Length - Case'), ('memory slots', 'Memory Slots - Motherboard'), ('motherboard support', 'Motherboard Support - Case'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('bearing type', 'Bearing Type - Cooler'), ('max memory', 'Max Memory - Motherboard'), ('resolution', 'Resolution - Monitor'), ('refresh rate', 'Refresh Rate - Monitor'), ('socket', 'Socket - Motherboard'), ('length', 'Length - GPU'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('memory interface', 'Memory Interface - GPU'), ('stream_processors', 'Stream Processors - GPU'), ('airflow', 'Airflow - Cooler'), ('powerConsumption', 'Power Consumption - GPU'), ('heat spreader', 'Heat Spreader - RAM'), ('noise level', 'Noise Level - Cooler'), ('tdp', 'TDP - CPU'), ('powerConsumption', 'Power Consumption - Motherboard'), ('latency', 'Latency - RAM'), ('type', 'Type - Storage'), ('modularity', 'Modularity - Power Supply'), ('wifi', 'WiFi - Motherboard'), ('max gpu length', 'Max GPU Length - Case'), ('front panel ports', 'Front Panel Ports - Case'), ('fan size', 'Fan Size - Cooler'), ('dimensions', 'Dimensions - Power Supply'), ('ports', 'Ports - GPU'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('type', 'Type - RAM'), ('controller', 'Controller - Storage'), ('cuda cores', 'CUDA Cores - GPU'), ('wattage', 'Wattage - Power Supply'), ('dimensions', 'Dimensions - Cooler'), ('voltage', 'Voltage - RAM'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('max cpu height', 'Max CPU Height - Case'), ('connectivity', 'Connectivity - Monitor'), ('powerConsumption', 'Power Consumption - CPU'), ('support', 'Support - Motherboard'), ('sata ports', 'SATA Ports - Motherboard'), ('form factor', 'Form Factor - Motherboard'), ('memory size', 'Memory Size - GPU'), ('cooling support', 'Cooling Support - Case'), ('read speed', 'Read Speed - Storage'), ('fan', 'Fan - Power Supply'), ('response time', 'Response Time - Monitor'), ('form factor', 'Form Factor - Case'), ('form factor', 'Form Factor - Storage'), ('modules', 'Modules - RAM'), ('usb ports', 'USB Ports - Motherboard'), ('certifications', 'Certifications - Power Supply'), ('chipset', 'Chipset - GPU'), ('size', 'Size - Monitor'), ('socket', 'Socket - CPU'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('type', 'Type - Cooler'), ('speed', 'Speed - RAM'), ('cache', 'Cache - CPU'), ('dimensions', 'Dimensions - Case')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
