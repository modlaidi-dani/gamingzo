# Generated by Django 4.2.5 on 2024-07-14 12:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('backendAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('write speed', 'Write Speed - Storage'), ('max memory', 'Max Memory - Motherboard'), ('dimensions', 'Dimensions - Power Supply'), ('response time', 'Response Time - Monitor'), ('radiator_size', 'Radiator Size - Cooler'), ('interface', 'Interface - Storage'), ('form factor', 'Form Factor - Storage'), ('memory speed', 'Memory Speed - Motherboard'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('powerConsumption', 'Power Consumption - GPU'), ('type', 'Type - Storage'), ('eco_mode', 'Eco Mode - Power Supply'), ('socket', 'Socket - Motherboard'), ('max cpu height', 'Max CPU Height - Case'), ('max psu length', 'Max PSU Length - Case'), ('connectivity', 'Connectivity - Monitor'), ('type', 'Type - Cooler'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('memory size', 'Memory Size - GPU'), ('warranty', 'Warranty - Power Supply'), ('tdp', 'TDP - CPU'), ('dimensions', 'Dimensions - Cooler'), ('rgb', 'RGB - RAM'), ('cache', 'Cache - CPU'), ('modules', 'Modules - RAM'), ('noise level', 'Noise Level - Cooler'), ('type', 'Type - Motherboard'), ('panel type', 'Panel Type - Monitor'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('chipset', 'Chipset - CPU'), ('certifications', 'Certifications - Power Supply'), ('rgb', 'RGB - Cooler'), ('fan size', 'Fan Size - Cooler'), ('latency', 'Latency - RAM'), ('memory slots', 'Memory Slots - Motherboard'), ('capacity', 'Capacity - RAM'), ('read speed', 'Read Speed - Storage'), ('type', 'Type - RAM'), ('architecture', 'Architecture - CPU'), ('fan size', 'Fan Size - Power Supply'), ('chipset', 'Chipset - Motherboard'), ('airflow', 'Airflow - Cooler'), ('wifi', 'WiFi - Motherboard'), ('powerConsumption', 'Power Consumption - Motherboard'), ('voltage', 'Voltage - RAM'), ('bearing type', 'Bearing Type - Cooler'), ('memory interface', 'Memory Interface - GPU'), ('lan', 'LAN - Motherboard'), ('motherboard support', 'Motherboard Support - Case'), ('cores', 'Cores - CPU'), ('expansion slots', 'Expansion Slots - Case'), ('resolution', 'Resolution - Monitor'), ('form factor', 'Form Factor - Motherboard'), ('powerConsumption', 'Power Consumption - Cooler'), ('heat spreader', 'Heat Spreader - RAM'), ('directx support', 'DirectX Support - GPU'), ('socket', 'Socket - CPU'), ('support', 'Support - Motherboard'), ('modularity', 'Modularity - Power Supply'), ('capacity', 'Capacity - Storage'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('dimensions', 'Dimensions - RAM'), ('form factor', 'Form Factor - Case'), ('memory type', 'Memory Type - GPU'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('cooling support', 'Cooling Support - Case'), ('size', 'Size - Monitor'), ('front panel ports', 'Front Panel Ports - Case'), ('wattage', 'Wattage - Power Supply'), ('dimensions', 'Dimensions - Case'), ('speed', 'Speed - RAM'), ('sata ports', 'SATA Ports - Motherboard'), ('powerConsumption', 'Power Consumption - CPU'), ('refresh rate', 'Refresh Rate - Monitor'), ('threads', 'Threads - CPU'), ('length', 'Length - GPU'), ('stream_processors', 'Stream Processors - GPU'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('ports', 'Ports - GPU'), ('max gpu length', 'Max GPU Length - Case'), ('chipset', 'Chipset - GPU'), ('drive bays', 'Drive Bays - Case'), ('controller', 'Controller - Storage'), ('usb ports', 'USB Ports - Motherboard'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('pcie slots', 'PCIe Slots - Motherboard'), ('fan', 'Fan - Power Supply'), ('form factor', 'Form Factor - Power Supply'), ('cuda cores', 'CUDA Cores - GPU')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
        migrations.CreateModel(
            name='SectionHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]
