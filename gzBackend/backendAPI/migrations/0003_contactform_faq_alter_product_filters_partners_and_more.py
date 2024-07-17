# Generated by Django 4.2.5 on 2024-07-14 13:01

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('backendAPI', '0002_alter_product_filters_sectionhome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=255, null=True)),
                ('dateSend', models.DateField()),
                ('phoneNumber', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(choices=[('en-attente', 'En Attente'), ('solved', 'Résolu')], max_length=255, null=True)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('show', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=wagtail.fields.StreamField([('filterS', wagtail.blocks.StructBlock([('filter_name', wagtail.blocks.ChoiceBlock(choices=[('wifi', 'WiFi - Motherboard'), ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'), ('efficiency rating', 'Efficiency Rating - Power Supply'), ('zero rpm mode', 'Zero RPM Mode - Power Supply'), ('dimensions', 'Dimensions - Case'), ('memory size', 'Memory Size - GPU'), ('powerConsumption', 'Power Consumption - Cooler'), ('fan size', 'Fan Size - Cooler'), ('interface', 'Interface - Storage'), ('type', 'Type - Motherboard'), ('capacity', 'Capacity - Storage'), ('length', 'Length - GPU'), ('sata ports', 'SATA Ports - Motherboard'), ('dimensions', 'Dimensions - Power Supply'), ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'), ('lan', 'LAN - Motherboard'), ('controller', 'Controller - Storage'), ('front panel ports', 'Front Panel Ports - Case'), ('fan', 'Fan - Power Supply'), ('form factor', 'Form Factor - Storage'), ('stream_processors', 'Stream Processors - GPU'), ('socket', 'Socket - CPU'), ('bearing type', 'Bearing Type - Cooler'), ('size', 'Size - Monitor'), ('dimensions', 'Dimensions - RAM'), ('refresh rate', 'Refresh Rate - Monitor'), ('eco_mode', 'Eco Mode - Power Supply'), ('type', 'Type - Cooler'), ('resolution', 'Resolution - Monitor'), ('dimensions', 'Dimensions - Cooler'), ('max gpu length', 'Max GPU Length - Case'), ('capacity', 'Capacity - RAM'), ('memory speed', 'Memory Speed - Motherboard'), ('motherboard support', 'Motherboard Support - Case'), ('modules', 'Modules - RAM'), ('airflow', 'Airflow - Cooler'), ('form factor', 'Form Factor - Motherboard'), ('drive bays', 'Drive Bays - Case'), ('powerConsumption', 'Power Consumption - Motherboard'), ('certifications', 'Certifications - Power Supply'), ('memory interface', 'Memory Interface - GPU'), ('noise level', 'Noise Level - Cooler'), ('modularity', 'Modularity - Power Supply'), ('expansion slots', 'Expansion Slots - Case'), ('form factor', 'Form Factor - Power Supply'), ('max psu length', 'Max PSU Length - Case'), ('warranty', 'Warranty - Power Supply'), ('max memory', 'Max Memory - Motherboard'), ('max cpu height', 'Max CPU Height - Case'), ('chipset', 'Chipset - Motherboard'), ('cores', 'Cores - CPU'), ('fan size', 'Fan Size - Power Supply'), ('aspect ratio', 'Aspect Ratio - Monitor'), ('type', 'Type - RAM'), ('radiator_size', 'Radiator Size - Cooler'), ('chipset', 'Chipset - GPU'), ('memory slots', 'Memory Slots - Motherboard'), ('response time', 'Response Time - Monitor'), ('read speed', 'Read Speed - Storage'), ('threads', 'Threads - CPU'), ('rgb', 'RGB - RAM'), ('memory type', 'Memory Type - GPU'), ('powerConsumption', 'Power Consumption - GPU'), ('connectivity', 'Connectivity - Monitor'), ('panel type', 'Panel Type - Monitor'), ('write speed', 'Write Speed - Storage'), ('cooling support', 'Cooling Support - Case'), ('m.2 slots', 'M.2 Slots - Motherboard'), ('pcie slots', 'PCIe Slots - Motherboard'), ('memory bandwidth', 'Memory Bandwidth - GPU'), ('cache', 'Cache - CPU'), ('speed', 'Speed - RAM'), ('support', 'Support - Motherboard'), ('usb ports', 'USB Ports - Motherboard'), ('voltage', 'Voltage - RAM'), ('type', 'Type - Storage'), ('cuda cores', 'CUDA Cores - GPU'), ('powerConsumption', 'Power Consumption - CPU'), ('architecture', 'Architecture - CPU'), ('wattage', 'Wattage - Power Supply'), ('rgb', 'RGB - Cooler'), ('socket', 'Socket - Motherboard'), ('directx support', 'DirectX Support - GPU'), ('form factor', 'Form Factor - Case'), ('ports', 'Ports - GPU'), ('chipset', 'Chipset - CPU'), ('tdp', 'TDP - CPU'), ('heat spreader', 'Heat Spreader - RAM'), ('latency', 'Latency - RAM')], label='Filter by Category', required=False)), ('value', wagtail.blocks.CharBlock(label='Filter Value'))]))], blank=True, use_json_field=True),
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255, null=True)),
                ('partner_link', models.CharField(max_length=255, null=True)),
                ('logo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255, null=True)),
                ('logo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]
