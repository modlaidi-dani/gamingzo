# Generated by Django 4.2.14 on 2024-07-24 15:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0066_alter_product_filters'),
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
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('response time', 'Response Time - Monitor'), ('directx support', 'DirectX Support - GPU'), ('resolution', 'Resolution - Monitor'), ('form factor', 'Form Factor - Storage'), ('fan size', 'Fan Size - Power Supply'), ('form factor', 'Form Factor - Power Supply'), ('form factor', 'Form Factor - Case'), ('max cpu height', 'Max CPU Height - Case'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('chipset', 'Chipset - GPU'), ('modules', 'Modules - RAM'), ('size', 'Size - Monitor'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('support', 'Support - Motherboard'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('latency', 'Latency - RAM'), ('usb ports', 'USB Ports - Motherboard'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('wifi', 'WiFi - Motherboard'), ('chipset', 'Chipset - CPU'), ('pcie slots', 'PCIe Slots - Motherboard'), ('stream_processors', 'Stream Processors - GPU'), ('max memory', 'Max Memory - Motherboard'), ('fan size', 'Fan Size - Cooler'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('modularity', 'Modularity - Power Supply'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('radiator_size', 'Radiator Size - Cooler'), ('socket', 'Socket - Motherboard'), ('memory interface', 'Memory Interface - GPU'), ('panel type', 'Panel Type - Monitor'), ('capacity', 'Capacity - RAM'), ('memory speed', 'Memory Speed - Motherboard'), ('powerConsumption', 'Power Consumption - Motherboard'), ('front panel ports', 'Front Panel Ports - Case'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('cuda cores', 'CUDA Cores - GPU'), ('certifications', 'Certifications - Power Supply'), ('drive bays', 'Drive Bays - Case'), ('read speed', 'Read Speed - Storage'), ('eco_mode', 'Eco Mode - Power Supply'), ('warranty', 'Warranty - Power Supply'), ('interface', 'Interface - Storage'), ('connectivity', 'Connectivity - Monitor'), ('type', 'Type - Motherboard'), ('threads', 'Threads - CPU'), ('ports', 'Ports - GPU'), ('sata ports', 'SATA Ports - Motherboard'), ('length', 'Length - GPU'), ('bearing type', 'Bearing Type - Cooler'), ('chipset', 'Chipset - Motherboard'), ('memory size', 'Memory Size - GPU'), ('cores', 'Cores - CPU'), ('cooling support', 'Cooling Support - Case'), ('controller', 'Controller - Storage'), ('powerConsumption', 'Power Consumption - Cooler'), ('expansion slots', 'Expansion Slots - Case'), ('type', 'Type - Storage'), ('airflow', 'Airflow - Cooler'), ('speed', 'Speed - RAM'), ('noise level', 'Noise Level - Cooler'), ('fan', 'Fan - Power Supply'), ('memory slots', 'Memory Slots - Motherboard'), ('memory type', 'Memory Type - GPU'), ('lan', 'LAN - Motherboard'), ('socket', 'Socket - CPU'), ('dimensions', 'Dimensions - Cooler'), ('write speed', 'Write Speed - Storage'), ('dimensions', 'Dimensions - Power Supply'), ('type', 'Type - RAM'), ('wattage', 'Wattage - Power Supply'), ('voltage', 'Voltage - RAM'), ('powerConsumption', 'Power Consumption - GPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('powerConsumption', 'Power Consumption - CPU'), ('dimensions', 'Dimensions - RAM'), ('form factor', 'Form Factor - Motherboard'), ('rgb', 'RGB - Cooler'), ('motherboard support', 'Motherboard Support - Case'), ('type', 'Type - Cooler'), ('max psu length', 'Max PSU Length - Case'), ('cache', 'Cache - CPU'), ('rgb', 'RGB - RAM'), ('max gpu length', 'Max GPU Length - Case'), ('architecture', 'Architecture - CPU'), ('capacity', 'Capacity - Storage'), ('tdp', 'TDP - CPU'), ('dimensions', 'Dimensions - Case'), ('heat spreader', 'Heat Spreader - RAM')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='productsincheckout',
            name='checkout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='backendAPI.checkoutinfo'),
        ),
    ]
