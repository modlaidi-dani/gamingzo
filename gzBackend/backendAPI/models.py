from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.blocks import StructBlock, CharBlock
from wagtail.models import Page
from wagtail.search import index
from modelcluster.models import ClusterableModel, ParentalManyToManyField
from taggit.managers import TaggableManager
from django import forms
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock,TextBlock, ListBlock, StreamBlock,ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from django.core.serializers.json import DjangoJSONEncoder
import json
from wagtail.images.models import Image  
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache

@register_snippet 
class Affiliation(models.Model):
    last_name=models.CharField(max_length=200,null=False)
    first_name=models.CharField(max_length=200,null=False)
    email=models.EmailField()
    phone_num=models.IntegerField(null=True)
    facebook=models.TextField()
    instagram=models.TextField()
    tiktok=models.TextField()
    youtube=models.TextField()
    def __str__(self) :
        return f"{self.last_name}  {self.first_name}"

@register_snippet 
class SectionHome(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    
@register_snippet 
class ContactForm(models.Model):
    State_CHOICES = {
        ('en-attente', 'En Attente'),
        ('solved', 'Résolu'),
    }            
    name = models.CharField(max_length=200, null=False,blank=False)
    date = models.DateField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=255, blank=False, null=True)
    company = models.CharField(max_length=200, null=False,blank=False)
    email=models.EmailField(blank=False)
    state = models.CharField(max_length=255 ,choices=State_CHOICES, null=True,default='en-attente')
    Message = models.TextField()
    
    def __str__(self) :
        return f"name: {self.name} company: {self.company} status: {self.state}  "
    
@register_snippet 
class Brands(models.Model):
    brand_name = models.CharField(max_length=255, blank=False, null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    ) 
    def __str__(self) -> str:
        return (self.brand_name)
    
@register_snippet 
class Partners(models.Model):
    partner_name = models.CharField(max_length=255, blank=False, null=True)
    partner_link = models.CharField(max_length=255, blank=False, null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    ) 

@register_snippet 
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    show = models.BooleanField(default=True)

@register_snippet    
class Category(models.Model):
    ROLE_CHOICES = (
        ('pc_concu', 'PC Pré-Conçu'),
        ('components', 'Composants'),
        ('peripheral', 'Périphériques'),
        ('audio', 'Audio & Screens'),
    )
    Components_CHOICES = (
        ('CPU', 'CPU'),
        ('GPU', 'GPU'),
        ('RAM', 'RAM'),
        ('storage', 'storage'),
        ('cooler', 'cooler'),
        ('power supply', 'power supply'),
        ('case', 'case'),
    )
    type = models.CharField(max_length=255, choices=ROLE_CHOICES, blank=False, null=True)
    label = models.CharField(max_length=255, blank=False, null=True)
    component = models.CharField(max_length=255, choices=Components_CHOICES, blank=False, null=True)
    categoryMere = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='categories_child'
    )
    
    def __str__(self):
        return "Catégorie: " + str(self.label) + ", Type = " + self.type  

class FilterBlock(StructBlock):
    FILTER_CHOICES = {
                ('tdp', 'TDP - CPU'),
                ('powerConsumption', 'Power Consumption - CPU'),
                ('architecture', 'Architecture - CPU'),
                ('socket', 'Socket - CPU'),
                ('cache', 'Cache - CPU'),
                ('cores', 'Cores - CPU'),
                ('threads', 'Threads - CPU'),
                ('chipset', 'Chipset - CPU'),
                ('support', 'Support - Motherboard'),
                ('powerConsumption', 'Power Consumption - Motherboard'),
                ('wifi', 'WiFi - Motherboard'),
                ('memory slots', 'Memory Slots - Motherboard'),
                ('form factor', 'Form Factor - Motherboard'),
                ('max memory', 'Max Memory - Motherboard'),
                ('socket', 'Socket - Motherboard'),
                ('pcie slots', 'PCIe Slots - Motherboard'),
                ('sata ports', 'SATA Ports - Motherboard'),
                ('type', 'Type - Motherboard'),
                ('lan', 'LAN - Motherboard'),
                ('usb ports', 'USB Ports - Motherboard'),
                ('memory speed', 'Memory Speed - Motherboard'),
                ('chipset', 'Chipset - Motherboard'),
                ('m.2 slots', 'M.2 Slots - Motherboard'),
                ('memory size', 'Memory Size - GPU'),
                ('memory type', 'Memory Type - GPU'),
                ('memory interface', 'Memory Interface - GPU'),
                ('powerConsumption', 'Power Consumption - GPU'),
                ('cuda cores', 'CUDA Cores - GPU'),
                ('length', 'Length - GPU'),
                ('directx support', 'DirectX Support - GPU'),
                ('ports', 'Ports - GPU'),
                ('stream_processors', 'Stream Processors - GPU'),
                ('memory bandwidth', 'Memory Bandwidth - GPU'),
                ('chipset', 'Chipset - GPU'),
                ('certifications', 'Certifications - Power Supply'),
                ('form factor', 'Form Factor - Power Supply'),
                ('fan', 'Fan - Power Supply'),
                ('fluid_dynamic_bearing_fan', 'Fluid Dynamic Bearing Fan - Power Supply'),
                ('dimensions', 'Dimensions - Power Supply'),
                ('warranty', 'Warranty - Power Supply'),
                ('fan size', 'Fan Size - Power Supply'),
                ('wattage', 'Wattage - Power Supply'),
                ('efficiency rating', 'Efficiency Rating - Power Supply'),
                ('modularity', 'Modularity - Power Supply'),
                ('eco_mode', 'Eco Mode - Power Supply'),
                ('zero rpm mode', 'Zero RPM Mode - Power Supply'),
                ('hybrid_silent_fan_control', 'Hybrid Silent Fan Control - Power Supply'),
                ('powerConsumption', 'Power Consumption - Cooler'),
                ('airflow', 'Airflow - Cooler'),
                ('rgb', 'RGB - Cooler'),
                ('dimensions', 'Dimensions - Cooler'),
                ('type', 'Type - Cooler'),
                ('fan size', 'Fan Size - Cooler'),
                ('noise level', 'Noise Level - Cooler'),
                ('bearing type', 'Bearing Type - Cooler'),
                ('radiator_size', 'Radiator Size - Cooler'),
                ('speed', 'Speed - RAM'),
                ('capacity', 'Capacity - RAM'),
                ('voltage', 'Voltage - RAM'),
                ('rgb', 'RGB - RAM'),
                ('heat spreader', 'Heat Spreader - RAM'),
                ('dimensions', 'Dimensions - RAM'),
                ('type', 'Type - RAM'),
                ('latency', 'Latency - RAM'),
                ('modules', 'Modules - RAM'),
                ('interface', 'Interface - Storage'),
                ('read speed', 'Read Speed - Storage'),
                ('form factor', 'Form Factor - Storage'),
                ('capacity', 'Capacity - Storage'),
                ('type', 'Type - Storage'),
                ('controller', 'Controller - Storage'),
                ('write speed', 'Write Speed - Storage'),
                ('max cpu height', 'Max CPU Height - Case'),
                ('motherboard support', 'Motherboard Support - Case'),
                ('cooling support', 'Cooling Support - Case'),
                ('form factor', 'Form Factor - Case'),
                ('drive bays', 'Drive Bays - Case'),
                ('dimensions', 'Dimensions - Case'),
                ('max psu length', 'Max PSU Length - Case'),
                ('front panel ports', 'Front Panel Ports - Case'),
                ('expansion slots', 'Expansion Slots - Case'),
                ('max gpu length', 'Max GPU Length - Case'),
                ('resolution', 'Resolution - Monitor'),
                ('response time', 'Response Time - Monitor'),
                ('panel type', 'Panel Type - Monitor'),
                ('connectivity', 'Connectivity - Monitor'),
                ('aspect ratio', 'Aspect Ratio - Monitor'),
                ('size', 'Size - Monitor'),
                ('refresh rate', 'Refresh Rate - Monitor'),

        }
    filter_name = ChoiceBlock(
        label='Filter by Category',
        required=False,
        choices=FILTER_CHOICES,
    )
    value = CharBlock(label="Filter Value")

class Product_Section(StructBlock):
    image = ImageChooserBlock()
    big_headline = TextBlock(blank=True)
    header = TextBlock(blank=True)
    caption = TextBlock(blank=True)

class Product_Galery(StructBlock):
    image = ImageChooserBlock()     

class ProductPageTag(TaggedItemBase):
    content_object = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='tagged_items')

class TechnicalSpecs(StructBlock):
    technical_name = TextBlock(blank=True)
    technical_value = TextBlock (blank=True)


@register_snippet
class Product(index.Indexed, ClusterableModel):
    reference = models.CharField(max_length=255, blank=False, null=True)
    designation = models.CharField(max_length=255, blank=False, null=True)
    header_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveBigIntegerField(blank=False, null=True, default=0)
    quantity = models.PositiveBigIntegerField(blank=False, null=True, default=0)
    price_promo = models.PositiveBigIntegerField(blank=False, null=True, default=0)
    new = models.BooleanField(verbose_name="New", default=False, null=True, blank=True)
    arrivage = models.BooleanField(verbose_name="Arrivage", default=False, null=True, blank=True)
    promo = models.BooleanField(verbose_name="Promotion", default=False, null=True, blank=True)
    config = models.BooleanField(verbose_name="Est une config", default=False, null=True, blank=True)
    support_page_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    related_product_pages = ParentalManyToManyField('self', blank=True)
    Product_In_Pc = ParentalManyToManyField('self', blank=True, related_name="mes_composants")
    body = StreamField([
        ('Product_Section', Product_Section()),
    ], use_json_field=True)
    
    gallery = StreamField([
        ('Product_Galery', Product_Galery()),
    ], use_json_field=True)

    filters = StreamField([
        ('filterS', FilterBlock()),
    ], blank=True, use_json_field=True)
    
    t_specs = StreamField([ 
        ('TechnicalSpecs', TechnicalSpecs()),
    ], blank=True, use_json_field=True)
    
    def __str__(self):
        return f"{self.reference}  {self.designation}"

    #------------------------- end of fields 
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('reference'),
            FieldPanel('category'),
            FieldPanel('description'),
        ], heading="Basics"),
        MultiFieldPanel([
            FieldPanel('price'),
            FieldPanel('price_promo'),
        ], heading="Pricing"),
        FieldRowPanel([
            FieldPanel('new'),
            FieldPanel('arrivage'),
            FieldPanel('promo'),
            FieldPanel('config'),
            FieldPanel('body'),
            FieldPanel('t_specs'),
        ], heading="Status"),
        MultiFieldPanel([
            FieldPanel('support_page_link'),
        ], heading="Support"),
        MultiFieldPanel([
            FieldPanel('related_product_pages', widget=forms.CheckboxSelectMultiple),
        ], heading="Related Products", classname="collapsed"),
        
    ]
    

    def get_filters(self):
        filters_dict = {}
        for block in self.filters:
            filters_dict[block.value['filter_name']] = block.value['value']
        return filters_dict

    def get_sections(self):
        sections = []
        for block in self.body:
            if block.block_type == 'Product_Section':    
                description_text = str(block.value.get("caption"))              
                big_headline = str(block.value.get("big_headline"))              
                header = str(block.value.get("header"))              
                image_url = str(block.value['image'].file.url)
                sections.append({
                    "description": description_text,
                    "big_headline": big_headline,
                    "header": header,               
                    "image": image_url,
                })
        return sections
    
    def get_specs(self):
        specs = []
        for block in self.t_specs:
            if block.block_type == 'TechnicalSpecs':    
                spec_name = str(block.value.get("technical_name"))              
                spec_value = str(block.value.get("technical_value"))              
                specs.append({
                    "spec_name": spec_name,
                    "spec_value": spec_value,               
                })
        return specs

    def get_image(self):
        first_image_url = 'http://127.0.0.1:8000/'+[block.value["image"].file.url for block in self.gallery][0]
        return first_image_url
    
    def get_gallery_images(self):
        return [block.image.url for block in self.gallery.all()]

    def to_json(self):
        return json.dumps(self.format_product_data(), cls=DjangoJSONEncoder)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
########

@register_snippet
class CheckoutInfo(models.Model):
    product=models.ManyToManyField(Product)
    dispatch=models.CharField(max_length=200, default='FromStore')
    total=models.IntegerField(default=0)
    first_name=models.CharField(max_length=200, null= False)
    last_name=models.CharField(max_length=200, null=False)
    wilaya=models.CharField(max_length=200,null=False)
    street=models.CharField(max_length=200,null=False)
    phone_num=models.CharField(max_length=200,null=False)
    email=models.EmailField()
    note=models.TextField()
    date=models.DateField( null=True, auto_now_add=True)
    def __str__(self):
        return f" name: {self.first_name} {self.last_name}  to:{self.wilaya}"
    
@register_snippet
class Newsletter(models.Model):
    email=models.EmailField()
    def __str__(self) -> str:
        return (self.email)    

@receiver(post_save, sender=Product)
def pre_save_handler(sender,instance, **kwargs):
        cache.clear()
        
@receiver(post_delete, sender=Product)
def pre_delete_handler(sender,instance, **kwargs):
        cache.clear()