from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .base import BaseList, BaseDetail
from app.models import DepartamentModel
from .serializers import DepartamentSerializer


class DepartamentList(BaseList):
    def __init__(self, **kwargs):
        super().__init__(DepartamentModel, DepartamentSerializer, **kwargs)

class DepartamentDetail(BaseDetail):
    def __init__(self, **kwargs):
        super().__init__(DepartamentModel, DepartamentSerializer, **kwargs)
