from django.db import models


class Service(models.Model):
    title = models.CharField('title', max_length=50)
    intro = models.TextField('intro')
    json_path = models.CharField('json with list')
    outro = models.TextField('outro')

    def __str__(self):
        return self.title
