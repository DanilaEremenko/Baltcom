from django.db import models


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=150)
    image_list = models.TextField('Список изображений в формате json')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
