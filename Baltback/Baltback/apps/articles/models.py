from django.db import models


class Article(models.Model):
    article_title = models.CharField('name of article', max_length=200)
    article_text = models.TextField('text of articles')
    pub_date = models.DateTimeField('date of publishing')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('authors name', max_length=200)
    comment_text = models.CharField('text of comment', max_length=200)
    pass
