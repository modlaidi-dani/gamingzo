# Generated by Django 4.2.14 on 2024-07-18 13:00

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0019_remove_checkoutinfo_product_alter_product_filters_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('motherboard support', 'Motherboard Support - Case'), ('voltage', 'Voltage - RAM'), ('speed', 'Speed - RAM'), ('tdp', 'TDP - CPU'), ('cooling support', 'Cooling Support - Case'), ('dimensions', 'Dimensions - RAM'), ('memory speed', 'Memory Speed - Motherboard'), ('type', 'Type - RAM'), ('drive bays', 'Drive Bays - Case'), ('ports', 'Ports - GPU'), ('type', 'Type - Storage'), ('stream_processors', 'Stream Processors - GPU'), ('expansion slots', 'Expansion Slots - Case'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('size', 'Size - Monitor'), ('lan', 'LAN - Motherboard'), ('max gpu length', 'Max GPU Length - Case'), ('memory interface', 'Memory Interface - GPU'), ('airflow', 'Airflow - Cooler'), ('powerConsumption', 'Power Consumption - Motherboard'), ('form factor', 'Form Factor - Motherboard'), ('form factor', 'Form Factor - Power Supply'), ('fan size', 'Fan Size - Cooler'), ('memory size', 'Memory Size - GPU'), ('latency', 'Latency - RAM'), ('panel type', 'Panel Type - Monitor'), ('dimensions', 'Dimensions - Power Supply'), ('capacity', 'Capacity - RAM'), ('form factor', 'Form Factor - Case'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('length', 'Length - GPU'), ('socket', 'Socket - CPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('sata ports', 'SATA Ports - Motherboard'), ('chipset', 'Chipset - GPU'), ('max cpu height', 'Max CPU Height - Case'), ('usb ports', 'USB Ports - Motherboard'), ('form factor', 'Form Factor - Storage'), ('read speed', 'Read Speed - Storage'), ('chipset', 'Chipset - CPU'), ('powerConsumption', 'Power Consumption - CPU'), ('powerConsumption', 'Power Consumption - GPU'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('connectivity', 'Connectivity - Monitor'), ('capacity', 'Capacity - Storage'), ('cuda cores', 'CUDA Cores - GPU'), ('directx support', 'DirectX Support - GPU'), ('heat spreader', 'Heat Spreader - RAM'), ('fan', 'Fan - Power Supply'), ('type', 'Type - Cooler'), ('rgb', 'RGB - RAM'), ('eco_mode', 'Eco Mode - Power Supply'), ('memory slots', 'Memory Slots - Motherboard'), ('resolution', 'Resolution - Monitor'), ('interface', 'Interface - Storage'), ('architecture', 'Architecture - CPU'), ('chipset', 'Chipset - Motherboard'), ('pcie slots', 'PCIe Slots - Motherboard'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('cores', 'Cores - CPU'), ('controller', 'Controller - Storage'), ('modules', 'Modules - RAM'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('radiator_size', 'Radiator Size - Cooler'), ('max psu length', 'Max PSU Length - Case'), ('max memory', 'Max Memory - Motherboard'), ('modularity', 'Modularity - Power Supply'), ('noise level', 'Noise Level - Cooler'), ('warranty', 'Warranty - Power Supply'), ('support', 'Support - Motherboard'), ('type', 'Type - Motherboard'), ('front panel ports', 'Front Panel Ports - Case'), ('write speed', 'Write Speed - Storage'), ('fan size', 'Fan Size - Power Supply'), ('dimensions', 'Dimensions - Case'), ('powerConsumption', 'Power Consumption - Cooler'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('threads', 'Threads - CPU'), ('response time', 'Response Time - Monitor'), ('bearing type', 'Bearing Type - Cooler'), ('dimensions', 'Dimensions - Cooler'), ('certifications', 'Certifications - Power Supply'), ('rgb', 'RGB - Cooler'), ('socket', 'Socket - Motherboard'), ('wifi', 'WiFi - Motherboard'), ('cache', 'Cache - CPU'), ('memory type', 'Memory Type - GPU'), ('wattage', 'Wattage - Power Supply')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
    ]
