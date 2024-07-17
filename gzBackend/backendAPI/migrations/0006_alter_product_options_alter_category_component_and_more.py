# Generated by Django 4.2.5 on 2024-07-14 15:06

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0005_remove_product_tags_alter_contactform_state_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='category',
            name='component',
            field=models.CharField(choices=[('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('storage', 'storage'), ('cooler', 'cooler'), ('power supply', 'power supply'), ('case', 'case')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('dimensions', 'Dimensions - Cooler'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('form factor', 'Form Factor - Storage'), ('type', 'Type - Motherboard'), ('fan', 'Fan - Power Supply'), ('interface', 'Interface - Storage'), ('write speed', 'Write Speed - Storage'), ('type', 'Type - Cooler'), ('drive bays', 'Drive Bays - Case'), ('form factor', 'Form Factor - Motherboard'), ('expansion slots', 'Expansion Slots - Case'), ('front panel ports', 'Front Panel Ports - Case'), ('chipset', 'Chipset - GPU'), ('usb ports', 'USB Ports - Motherboard'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('length', 'Length - GPU'), ('directx support', 'DirectX Support - GPU'), ('form factor', 'Form Factor - Power Supply'), ('wifi', 'WiFi - Motherboard'), ('chipset', 'Chipset - CPU'), ('cuda cores', 'CUDA Cores - GPU'), ('architecture', 'Architecture - CPU'), ('size', 'Size - Monitor'), ('bearing type', 'Bearing Type - Cooler'), ('fan size', 'Fan Size - Cooler'), ('dimensions', 'Dimensions - Case'), ('form factor', 'Form Factor - Case'), ('powerConsumption', 'Power Consumption - GPU'), ('sata ports', 'SATA Ports - Motherboard'), ('socket', 'Socket - Motherboard'), ('support', 'Support - Motherboard'), ('modules', 'Modules - RAM'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('airflow', 'Airflow - Cooler'), ('cores', 'Cores - CPU'), ('type', 'Type - RAM'), ('modularity', 'Modularity - Power Supply'), ('dimensions', 'Dimensions - Power Supply'), ('rgb', 'RGB - Cooler'), ('fan size', 'Fan Size - Power Supply'), ('controller', 'Controller - Storage'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('threads', 'Threads - CPU'), ('response time', 'Response Time - Monitor'), ('memory interface', 'Memory Interface - GPU'), ('memory slots', 'Memory Slots - Motherboard'), ('eco_mode', 'Eco Mode - Power Supply'), ('capacity', 'Capacity - Storage'), ('rgb', 'RGB - RAM'), ('max memory', 'Max Memory - Motherboard'), ('chipset', 'Chipset - Motherboard'), ('stream_processors', 'Stream Processors - GPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('voltage', 'Voltage - RAM'), ('memory size', 'Memory Size - GPU'), ('noise level', 'Noise Level - Cooler'), ('radiator_size', 'Radiator Size - Cooler'), ('lan', 'LAN - Motherboard'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('capacity', 'Capacity - RAM'), ('connectivity', 'Connectivity - Monitor'), ('motherboard support', 'Motherboard Support - Case'), ('memory type', 'Memory Type - GPU'), ('max gpu length', 'Max GPU Length - Case'), ('powerConsumption', 'Power Consumption - Cooler'), ('certifications', 'Certifications - Power Supply'), ('heat spreader', 'Heat Spreader - RAM'), ('memory speed', 'Memory Speed - Motherboard'), ('ports', 'Ports - GPU'), ('type', 'Type - Storage'), ('powerConsumption', 'Power Consumption - CPU'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('pcie slots', 'PCIe Slots - Motherboard'), ('socket', 'Socket - CPU'), ('cooling support', 'Cooling Support - Case'), ('wattage', 'Wattage - Power Supply'), ('powerConsumption', 'Power Consumption - Motherboard'), ('dimensions', 'Dimensions - RAM'), ('warranty', 'Warranty - Power Supply'), ('tdp', 'TDP - CPU'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('latency', 'Latency - RAM'), ('cache', 'Cache - CPU'), ('panel type', 'Panel Type - Monitor'), ('resolution', 'Resolution - Monitor'), ('max psu length', 'Max PSU Length - Case'), ('read speed', 'Read Speed - Storage'), ('max cpu height', 'Max CPU Height - Case'), ('speed', 'Speed - RAM')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
        migrations.DeleteModel(
            name='Components',
        ),
    ]
