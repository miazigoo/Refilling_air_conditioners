from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'))
    service_name = models.CharField(_('Опция услуги'), max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Услугу')
        verbose_name_plural = _('Услуги')


class PricingTableEntry(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='prices',
        verbose_name=_('Услуга')
    )
    weight_range = models.CharField(_('Диапазон веса'), max_length=50)
    price = models.CharField(_('Цена'), max_length=50)

    def __str__(self):
        return f"{self.service.title}, {self.weight_range}: {self.price}"

    class Meta:
        verbose_name = _('Строки прайс-листа')
        verbose_name_plural = _('Таблицы цен')

class ContactInfo(models.Model):
    phone = models.CharField(_('Телефон'), max_length=20)
    email = models.EmailField(_('E-mail'))
    address = models.TextField(_('Адрес'))

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Контактная информация')
        verbose_name_plural = _('Контактные данные')