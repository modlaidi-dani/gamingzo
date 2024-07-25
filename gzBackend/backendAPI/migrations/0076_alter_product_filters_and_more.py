# Generated by Django 4.2.14 on 2024-07-25 12:17

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0075_alter_contactform_state_alter_product_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('rgb', 'RGB - RAM'), ('support', 'Support - Motherboard'), ('drive bays', 'Drive Bays - Case'), ('wifi', 'WiFi - Motherboard'), ('chipset', 'Chipset - GPU'), ('memory speed', 'Memory Speed - Motherboard'), ('modularity', 'Modularity - Power Supply'), ('certifications', 'Certifications - Power Supply'), ('max psu length', 'Max PSU Length - Case'), ('rgb', 'RGB - Cooler'), ('read speed', 'Read Speed - Storage'), ('max cpu height', 'Max CPU Height - Case'), ('powerConsumption', 'Power Consumption - GPU'), ('memory size', 'Memory Size - GPU'), ('socket', 'Socket - Motherboard'), ('noise level', 'Noise Level - Cooler'), ('motherboard support', 'Motherboard Support - Case'), ('airflow', 'Airflow - Cooler'), ('wattage', 'Wattage - Power Supply'), ('modules', 'Modules - RAM'), ('memory type', 'Memory Type - GPU'), ('size', 'Size - Monitor'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('form factor', 'Form Factor - Storage'), ('panel type', 'Panel Type - Monitor'), ('form factor', 'Form Factor - Power Supply'), ('eco_mode', 'Eco Mode - Power Supply'), ('type', 'Type - RAM'), ('architecture', 'Architecture - CPU'), ('powerConsumption', 'Power Consumption - Motherboard'), ('cooling support', 'Cooling Support - Case'), ('chipset', 'Chipset - CPU'), ('cuda cores', 'CUDA Cores - GPU'), ('form factor', 'Form Factor - Case'), ('heat spreader', 'Heat Spreader - RAM'), ('cores', 'Cores - CPU'), ('capacity', 'Capacity - RAM'), ('warranty', 'Warranty - Power Supply'), ('cache', 'Cache - CPU'), ('memory slots', 'Memory Slots - Motherboard'), ('memory interface', 'Memory Interface - GPU'), ('capacity', 'Capacity - Storage'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('dimensions', 'Dimensions - Cooler'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('connectivity', 'Connectivity - Monitor'), ('dimensions', 'Dimensions - Case'), ('type', 'Type - Motherboard'), ('max gpu length', 'Max GPU Length - Case'), ('threads', 'Threads - CPU'), ('radiator_size', 'Radiator Size - Cooler'), ('bearing type', 'Bearing Type - Cooler'), ('type', 'Type - Storage'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('stream_processors', 'Stream Processors - GPU'), ('interface', 'Interface - Storage'), ('refresh rate', 'Refresh Rate - Monitor'), ('ports', 'Ports - GPU'), ('powerConsumption', 'Power Consumption - CPU'), ('sata ports', 'SATA Ports - Motherboard'), ('latency', 'Latency - RAM'), ('resolution', 'Resolution - Monitor'), ('type', 'Type - Cooler'), ('chipset', 'Chipset - Motherboard'), ('expansion slots', 'Expansion Slots - Case'), ('length', 'Length - GPU'), ('voltage', 'Voltage - RAM'), ('front panel ports', 'Front Panel Ports - Case'), ('tdp', 'TDP - CPU'), ('fan size', 'Fan Size - Power Supply'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('max memory', 'Max Memory - Motherboard'), ('socket', 'Socket - CPU'), ('powerConsumption', 'Power Consumption - Cooler'), ('form factor', 'Form Factor - Motherboard'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('controller', 'Controller - Storage'), ('fan size', 'Fan Size - Cooler'), ('response time', 'Response Time - Monitor'), ('write speed', 'Write Speed - Storage'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('fan', 'Fan - Power Supply'), ('speed', 'Speed - RAM'), ('dimensions', 'Dimensions - RAM'), ('directx support', 'DirectX Support - GPU'), ('lan', 'LAN - Motherboard'), ('usb ports', 'USB Ports - Motherboard'), ('pcie slots', 'PCIe Slots - Motherboard'), ('dimensions', 'Dimensions - Power Supply')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='productsincheckout',
            name='checkout',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='backendAPI.checkoutinfo'),
        ),
    ]
