# Generated by Django 4.2.14 on 2024-07-21 09:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0032_alter_product_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('m.2 slots', 'M.2 Slots - Motherboard'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('connectivity', 'Connectivity - Monitor'), ('memory type', 'Memory Type - GPU'), ('ports', 'Ports - GPU'), ('wattage', 'Wattage - Power Supply'), ('voltage', 'Voltage - RAM'), ('rgb', 'RGB - RAM'), ('powerConsumption', 'Power Consumption - GPU'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('length', 'Length - GPU'), ('max memory', 'Max Memory - Motherboard'), ('tdp', 'TDP - CPU'), ('resolution', 'Resolution - Monitor'), ('socket', 'Socket - CPU'), ('write speed', 'Write Speed - Storage'), ('usb ports', 'USB Ports - Motherboard'), ('chipset', 'Chipset - GPU'), ('dimensions', 'Dimensions - RAM'), ('size', 'Size - Monitor'), ('capacity', 'Capacity - RAM'), ('memory size', 'Memory Size - GPU'), ('cooling support', 'Cooling Support - Case'), ('max psu length', 'Max PSU Length - Case'), ('bearing type', 'Bearing Type - Cooler'), ('memory interface', 'Memory Interface - GPU'), ('form factor', 'Form Factor - Storage'), ('radiator_size', 'Radiator Size - Cooler'), ('threads', 'Threads - CPU'), ('max cpu height', 'Max CPU Height - Case'), ('front panel ports', 'Front Panel Ports - Case'), ('fan', 'Fan - Power Supply'), ('powerConsumption', 'Power Consumption - Cooler'), ('powerConsumption', 'Power Consumption - CPU'), ('modularity', 'Modularity - Power Supply'), ('drive bays', 'Drive Bays - Case'), ('form factor', 'Form Factor - Power Supply'), ('capacity', 'Capacity - Storage'), ('read speed', 'Read Speed - Storage'), ('architecture', 'Architecture - CPU'), ('form factor', 'Form Factor - Motherboard'), ('type', 'Type - Cooler'), ('expansion slots', 'Expansion Slots - Case'), ('max gpu length', 'Max GPU Length - Case'), ('controller', 'Controller - Storage'), ('wifi', 'WiFi - Motherboard'), ('fan size', 'Fan Size - Cooler'), ('speed', 'Speed - RAM'), ('modules', 'Modules - RAM'), ('form factor', 'Form Factor - Case'), ('noise level', 'Noise Level - Cooler'), ('memory speed', 'Memory Speed - Motherboard'), ('latency', 'Latency - RAM'), ('airflow', 'Airflow - Cooler'), ('heat spreader', 'Heat Spreader - RAM'), ('cores', 'Cores - CPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('stream_processors', 'Stream Processors - GPU'), ('dimensions', 'Dimensions - Power Supply'), ('fan size', 'Fan Size - Power Supply'), ('certifications', 'Certifications - Power Supply'), ('cuda cores', 'CUDA Cores - GPU'), ('type', 'Type - Storage'), ('dimensions', 'Dimensions - Cooler'), ('rgb', 'RGB - Cooler'), ('chipset', 'Chipset - CPU'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('motherboard support', 'Motherboard Support - Case'), ('interface', 'Interface - Storage'), ('lan', 'LAN - Motherboard'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('cache', 'Cache - CPU'), ('chipset', 'Chipset - Motherboard'), ('type', 'Type - Motherboard'), ('socket', 'Socket - Motherboard'), ('sata ports', 'SATA Ports - Motherboard'), ('eco_mode', 'Eco Mode - Power Supply'), ('support', 'Support - Motherboard'), ('directx support', 'DirectX Support - GPU'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('powerConsumption', 'Power Consumption - Motherboard'), ('response time', 'Response Time - Monitor'), ('dimensions', 'Dimensions - Case'), ('pcie slots', 'PCIe Slots - Motherboard'), ('memory slots', 'Memory Slots - Motherboard'), ('panel type', 'Panel Type - Monitor'), ('warranty', 'Warranty - Power Supply'), ('type', 'Type - RAM')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
