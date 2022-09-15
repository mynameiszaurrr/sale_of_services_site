from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, help_text='Название услуги', verbose_name='Название')
    description = models.TextField(max_length=200, help_text='Описание услуги', verbose_name='Описание')
    price = models.IntegerField(help_text='Цена за услугу в КОПЕЙКАХ', verbose_name='Цена')

    def __str__(self):
        return self.name


class ItemAPI(models.Model):
    api_id = models.CharField(max_length=100, help_text='API ID продукта', verbose_name='API ID')
    name = models.OneToOneField(Item, on_delete=models.PROTECT, primary_key=True)