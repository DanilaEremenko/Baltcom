from django.db import models


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=50)
    intro = models.TextField('Введение')
    enum_json = models.TextField("Перечисление в формате json")
    outro = models.TextField('Подытоживание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
