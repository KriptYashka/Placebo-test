from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

def index_page(request: WSGIRequest):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context)
