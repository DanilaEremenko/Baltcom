from django.db import models


class News(models.Model):
    title = models.CharField('title', max_length=150)
    text = models.TextField('text')
    pub_date = models.DateTimeField('date of publishing')

    def __str__(self):
        return self.title
