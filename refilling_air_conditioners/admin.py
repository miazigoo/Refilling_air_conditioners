from django.contrib import admin
from .models import Service, PricingTableEntry, ContactInfo

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(PricingTableEntry)
class PricingTableEntryAdmin(admin.ModelAdmin):
    list_display = ('weight_range', 'service', 'price')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
