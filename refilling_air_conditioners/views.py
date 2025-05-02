from django.shortcuts import render
from .models import Service, PricingTableEntry, ContactInfo

def index(request):
    services = Service.objects.all()  # Получаем все услуги
    pricing_table = PricingTableEntry.objects.all().order_by('id')  # Получаем таблицу цен
    contact_info = ContactInfo.objects.first()  # Берём первую запись контактов (предположительно одну единственную)

    context = {
        'services': services,
        'pricing_table': pricing_table,
        'contact_info': contact_info
    }
    return render(request, 'index.html', context)