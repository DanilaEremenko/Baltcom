from django.http import HttpResponse
from .models import Product
import json


def index(request):
    mode = 'db'
    http_resp = "<h1>Наша продукция</h1>\n"

    if mode == 'db':
        for product in Product.objects.all().order_by('id'):
            http_resp += "<h2>%s</h2>\n" % product.title
            for image_path in json.loads(product.image_list).get("image_list"):
                http_resp += "<img src=\"/static/%s\">\n" % image_path
    elif mode == 'json':
        http_resp = "TODO"

    return HttpResponse(http_resp)
