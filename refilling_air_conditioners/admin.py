from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service, PricingTableEntry, ContactInfo, CarouselImg

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(PricingTableEntry)
class PricingTableEntryAdmin(admin.ModelAdmin):
    list_display = ('weight_range', 'service', 'price')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')


@admin.register(CarouselImg)
class CarouselImgAdmin(admin.ModelAdmin):
    list_display = ("get_image",)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url}  height="60"')

    get_image.short_description = "Изображение"


admin.site.site_title = "Заправка кондиционеров"
admin.site.site_header = "Заправка кондиционеров"