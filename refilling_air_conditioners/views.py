from django.shortcuts import render
from .models import Service, PricingTableEntry, ContactInfo, CarouselImg

def index(request):
    services = Service.objects.all()  # Получаем все услуги
    pricing_table = PricingTableEntry.objects.all().order_by('id')  # Получаем таблицу цен
    contact_info = ContactInfo.objects.first()  # Берём первую запись контактов (предположительно одну единственную)
    carousel_images = CarouselImg.objects.all()  # Все изображения карусели

    # Преобразование queryset в простой список с нужными полями
    imgs = [
        {'url': img.image.url, 'id': idx}
        for idx, img in enumerate(carousel_images)
    ]

    print(len(imgs))
    print(imgs)

    context = {
        'images': imgs,
        'services': services,
        'pricing_table': pricing_table,
        'contact_info': contact_info,

    }
    return render(request, 'index.html', context)