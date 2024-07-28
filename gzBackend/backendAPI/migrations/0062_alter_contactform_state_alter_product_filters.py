# Generated by Django 4.2.14 on 2024-07-24 14:26

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0061_alter_product_filters'),
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
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('modularity', 'Modularity - Power Supply'), ('certifications', 'Certifications - Power Supply'), ('powerConsumption', 'Power Consumption - Cooler'), ('form factor', 'Form Factor - Case'), ('powerConsumption', 'Power Consumption - GPU'), ('memory size', 'Memory Size - GPU'), ('dimensions', 'Dimensions - Case'), ('stream_processors', 'Stream Processors - GPU'), ('resolution', 'Resolution - Monitor'), ('tdp', 'TDP - CPU'), ('fan', 'Fan - Power Supply'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('max cpu height', 'Max CPU Height - Case'), ('ports', 'Ports - GPU'), ('wattage', 'Wattage - Power Supply'), ('noise level', 'Noise Level - Cooler'), ('motherboard support', 'Motherboard Support - Case'), ('airflow', 'Airflow - Cooler'), ('drive bays', 'Drive Bays - Case'), ('front panel ports', 'Front Panel Ports - Case'), ('response time', 'Response Time - Monitor'), ('wifi', 'WiFi - Motherboard'), ('lan', 'LAN - Motherboard'), ('sata ports', 'SATA Ports - Motherboard'), ('usb ports', 'USB Ports - Motherboard'), ('powerConsumption', 'Power Consumption - CPU'), ('speed', 'Speed - RAM'), ('cooling support', 'Cooling Support - Case'), ('dimensions', 'Dimensions - Cooler'), ('memory slots', 'Memory Slots - Motherboard'), ('interface', 'Interface - Storage'), ('form factor', 'Form Factor - Motherboard'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('modules', 'Modules - RAM'), ('rgb', 'RGB - Cooler'), ('pcie slots', 'PCIe Slots - Motherboard'), ('voltage', 'Voltage - RAM'), ('radiator_size', 'Radiator Size - Cooler'), ('capacity', 'Capacity - Storage'), ('type', 'Type - Cooler'), ('form factor', 'Form Factor - Power Supply'), ('type', 'Type - Motherboard'), ('memory speed', 'Memory Speed - Motherboard'), ('refresh rate', 'Refresh Rate - Monitor'), ('connectivity', 'Connectivity - Monitor'), ('expansion slots', 'Expansion Slots - Case'), ('type', 'Type - RAM'), ('dimensions', 'Dimensions - Power Supply'), ('socket', 'Socket - Motherboard'), ('support', 'Support - Motherboard'), ('chipset', 'Chipset - CPU'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('bearing type', 'Bearing Type - Cooler'), ('fan size', 'Fan Size - Cooler'), ('chipset', 'Chipset - Motherboard'), ('eco_mode', 'Eco Mode - Power Supply'), ('directx support', 'DirectX Support - GPU'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('memory interface', 'Memory Interface - GPU'), ('threads', 'Threads - CPU'), ('powerConsumption', 'Power Consumption - Motherboard'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('form factor', 'Form Factor - Storage'), ('chipset', 'Chipset - GPU'), ('panel type', 'Panel Type - Monitor'), ('cores', 'Cores - CPU'), ('write speed', 'Write Speed - Storage'), ('fan size', 'Fan Size - Power Supply'), ('read speed', 'Read Speed - Storage'), ('warranty', 'Warranty - Power Supply'), ('socket', 'Socket - CPU'), ('type', 'Type - Storage'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('rgb', 'RGB - RAM'), ('heat spreader', 'Heat Spreader - RAM'), ('latency', 'Latency - RAM'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('max psu length', 'Max PSU Length - Case'), ('architecture', 'Architecture - CPU'), ('controller', 'Controller - Storage'), ('memory type', 'Memory Type - GPU'), ('max gpu length', 'Max GPU Length - Case'), ('dimensions', 'Dimensions - RAM'), ('size', 'Size - Monitor'), ('max memory', 'Max Memory - Motherboard'), ('capacity', 'Capacity - RAM'), ('length', 'Length - GPU'), ('cache', 'Cache - CPU'), ('cuda cores', 'CUDA Cores - GPU')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
