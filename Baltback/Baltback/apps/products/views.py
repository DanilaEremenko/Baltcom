from django.http import HttpResponse
from .models import Product
import json


def index(request):
    mode = 'db'
    http_resp = "<h1>Наша продукция</h1>"

    if mode == 'db':
        for product in Product.objects.all():
            http_resp += "<h2>%s</h2>\n" % product.title
            # http_resp += "{% load static %}\n"
            for image_path in json.loads(product.image_list).get("image_list"):
                http_resp += "<img src=\"{% static \"media/products/TEC_DIZEL/cer1.jpg\" %}\">"
    elif mode == 'json':
        http_resp = "TODO"

    return HttpResponse(http_resp)
