from django.http import HttpResponse
import json


def index(request):
    with open('Baltback/apps/services/res/services.json') as services_json:
        d = dict(json.load(services_json))
        http_resp = ""
        for service in d.get("services"):
            http_resp += "<h1>%s</h1>\n" % service.get("name")
            http_resp += "<h2>%s</h2>\n" % service.get("intro")
            http_resp += "<ul>\n"
            for serv_desc in service.get("service_list"):
                http_resp += "<li>%s</li>\n" % serv_desc
            http_resp += "</ul>\n"
            http_resp += "<h2>%s</h2>\n\n\n" % service.get("outro")

    return HttpResponse(http_resp)
