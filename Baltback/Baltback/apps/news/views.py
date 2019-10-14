from django.http import HttpResponse
from .models import Article


def index(request):
    http_resp = ""
    for news in Article.objects.all():
        http_resp += "<h1>%s</h1>\n" % news.title
        http_resp += "<i>%s</i>\n" % news.text
        http_resp += "<br><b>%s</b>\n" % news.pub_date

    return HttpResponse(http_resp)
