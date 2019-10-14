from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
