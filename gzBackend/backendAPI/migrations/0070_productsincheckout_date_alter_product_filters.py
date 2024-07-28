# Generated by Django 4.2.14 on 2024-07-25 10:02

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0069_alter_contactform_state_alter_product_filters'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsincheckout',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('support', 'Support - Motherboard'), ('memory interface', 'Memory Interface - GPU'), ('dimensions', 'Dimensions - Cooler'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('length', 'Length - GPU'), ('front panel ports', 'Front Panel Ports - Case'), ('interface', 'Interface - Storage'), ('socket', 'Socket - CPU'), ('capacity', 'Capacity - RAM'), ('latency', 'Latency - RAM'), ('chipset', 'Chipset - GPU'), ('architecture', 'Architecture - CPU'), ('rgb', 'RGB - Cooler'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('max psu length', 'Max PSU Length - Case'), ('wattage', 'Wattage - Power Supply'), ('read speed', 'Read Speed - Storage'), ('powerConsumption', 'Power Consumption - CPU'), ('form factor', 'Form Factor - Motherboard'), ('speed', 'Speed - RAM'), ('type', 'Type - Storage'), ('chipset', 'Chipset - Motherboard'), ('wifi', 'WiFi - Motherboard'), ('form factor', 'Form Factor - Storage'), ('airflow', 'Airflow - Cooler'), ('powerConsumption', 'Power Consumption - Motherboard'), ('max gpu length', 'Max GPU Length - Case'), ('lan', 'LAN - Motherboard'), ('cores', 'Cores - CPU'), ('panel type', 'Panel Type - Monitor'), ('warranty', 'Warranty - Power Supply'), ('size', 'Size - Monitor'), ('refresh rate', 'Refresh Rate - Monitor'), ('modules', 'Modules - RAM'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('fan', 'Fan - Power Supply'), ('directx support', 'DirectX Support - GPU'), ('expansion slots', 'Expansion Slots - Case'), ('noise level', 'Noise Level - Cooler'), ('response time', 'Response Time - Monitor'), ('bearing type', 'Bearing Type - Cooler'), ('pcie slots', 'PCIe Slots - Motherboard'), ('capacity', 'Capacity - Storage'), ('form factor', 'Form Factor - Case'), ('eco_mode', 'Eco Mode - Power Supply'), ('usb ports', 'USB Ports - Motherboard'), ('max cpu height', 'Max CPU Height - Case'), ('memory size', 'Memory Size - GPU'), ('cooling support', 'Cooling Support - Case'), ('rgb', 'RGB - RAM'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('write speed', 'Write Speed - Storage'), ('threads', 'Threads - CPU'), ('dimensions', 'Dimensions - Power Supply'), ('certifications', 'Certifications - Power Supply'), ('cuda cores', 'CUDA Cores - GPU'), ('voltage', 'Voltage - RAM'), ('resolution', 'Resolution - Monitor'), ('motherboard support', 'Motherboard Support - Case'), ('controller', 'Controller - Storage'), ('drive bays', 'Drive Bays - Case'), ('type', 'Type - Motherboard'), ('socket', 'Socket - Motherboard'), ('memory speed', 'Memory Speed - Motherboard'), ('powerConsumption', 'Power Consumption - GPU'), ('tdp', 'TDP - CPU'), ('ports', 'Ports - GPU'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('type', 'Type - Cooler'), ('powerConsumption', 'Power Consumption - Cooler'), ('stream_processors', 'Stream Processors - GPU'), ('max memory', 'Max Memory - Motherboard'), ('memory slots', 'Memory Slots - Motherboard'), ('dimensions', 'Dimensions - RAM'), ('fan size', 'Fan Size - Power Supply'), ('chipset', 'Chipset - CPU'), ('form factor', 'Form Factor - Power Supply'), ('fan size', 'Fan Size - Cooler'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('connectivity', 'Connectivity - Monitor'), ('sata ports', 'SATA Ports - Motherboard'), ('modularity', 'Modularity - Power Supply'), ('heat spreader', 'Heat Spreader - RAM'), ('type', 'Type - RAM'), ('dimensions', 'Dimensions - Case'), ('memory type', 'Memory Type - GPU'), ('cache', 'Cache - CPU'), ('radiator_size', 'Radiator Size - Cooler')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
