# Generated by Django 4.2.14 on 2024-07-22 08:53

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0041_alter_contactform_state_alter_product_filters'),
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
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('motherboard support', 'Motherboard Support - Case'), ('fan size', 'Fan Size - Power Supply'), ('cores', 'Cores - CPU'), ('modularity', 'Modularity - Power Supply'), ('socket', 'Socket - Motherboard'), ('capacity', 'Capacity - Storage'), ('form factor', 'Form Factor - Case'), ('voltage', 'Voltage - RAM'), ('powerConsumption', 'Power Consumption - Motherboard'), ('ports', 'Ports - GPU'), ('wattage', 'Wattage - Power Supply'), ('interface', 'Interface - Storage'), ('latency', 'Latency - RAM'), ('chipset', 'Chipset - GPU'), ('bearing type', 'Bearing Type - Cooler'), ('dimensions', 'Dimensions - Case'), ('certifications', 'Certifications - Power Supply'), ('type', 'Type - Storage'), ('rgb', 'RGB - RAM'), ('architecture', 'Architecture - CPU'), ('heat spreader', 'Heat Spreader - RAM'), ('controller', 'Controller - Storage'), ('eco_mode', 'Eco Mode - Power Supply'), ('airflow', 'Airflow - Cooler'), ('connectivity', 'Connectivity - Monitor'), ('panel type', 'Panel Type - Monitor'), ('dimensions', 'Dimensions - Power Supply'), ('stream_processors', 'Stream Processors - GPU'), ('memory slots', 'Memory Slots - Motherboard'), ('noise level', 'Noise Level - Cooler'), ('max memory', 'Max Memory - Motherboard'), ('support', 'Support - Motherboard'), ('form factor', 'Form Factor - Storage'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('form factor', 'Form Factor - Power Supply'), ('resolution', 'Resolution - Monitor'), ('read speed', 'Read Speed - Storage'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('dimensions', 'Dimensions - Cooler'), ('form factor', 'Form Factor - Motherboard'), ('max gpu length', 'Max GPU Length - Case'), ('cooling support', 'Cooling Support - Case'), ('drive bays', 'Drive Bays - Case'), ('max psu length', 'Max PSU Length - Case'), ('radiator_size', 'Radiator Size - Cooler'), ('memory size', 'Memory Size - GPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('wifi', 'WiFi - Motherboard'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('type', 'Type - RAM'), ('type', 'Type - Motherboard'), ('cache', 'Cache - CPU'), ('max cpu height', 'Max CPU Height - Case'), ('chipset', 'Chipset - Motherboard'), ('threads', 'Threads - CPU'), ('front panel ports', 'Front Panel Ports - Case'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('sata ports', 'SATA Ports - Motherboard'), ('powerConsumption', 'Power Consumption - GPU'), ('warranty', 'Warranty - Power Supply'), ('dimensions', 'Dimensions - RAM'), ('socket', 'Socket - CPU'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('response time', 'Response Time - Monitor'), ('size', 'Size - Monitor'), ('speed', 'Speed - RAM'), ('memory type', 'Memory Type - GPU'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('modules', 'Modules - RAM'), ('fan', 'Fan - Power Supply'), ('lan', 'LAN - Motherboard'), ('memory speed', 'Memory Speed - Motherboard'), ('type', 'Type - Cooler'), ('powerConsumption', 'Power Consumption - CPU'), ('pcie slots', 'PCIe Slots - Motherboard'), ('powerConsumption', 'Power Consumption - Cooler'), ('capacity', 'Capacity - RAM'), ('fan size', 'Fan Size - Cooler'), ('memory interface', 'Memory Interface - GPU'), ('tdp', 'TDP - CPU'), ('directx support', 'DirectX Support - GPU'), ('usb ports', 'USB Ports - Motherboard'), ('expansion slots', 'Expansion Slots - Case'), ('rgb', 'RGB - Cooler'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('length', 'Length - GPU'), ('cuda cores', 'CUDA Cores - GPU'), ('write speed', 'Write Speed - Storage'), ('chipset', 'Chipset - CPU')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
