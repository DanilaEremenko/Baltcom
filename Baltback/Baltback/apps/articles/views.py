from django.http import HttpResponse
from .models import Article


def index(request):
    http_resp_text = ''
    for article in Article.objects.all():
        http_resp_text += "<h1>%s<h1>\n" % article.article_title
    return HttpResponse(http_resp_text)


def texts(request):
    http_resp_text = ''
    for article in Article.objects.all():
        http_resp_text += "<h3>%s<h3>\n\n\n" % article.article_text
    return HttpResponse(http_resp_text)
