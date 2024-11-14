from django.core.handlers.wsgi import WSGIRequest
from django.core.serializers import serialize
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import DepartamentModel
from .serializers import DepartamentSerializer


class DepartamentList(APIView):
    def get(self, request: WSGIRequest):
        queryset = DepartamentModel.objects.all()
        serializer_for_queryset = DepartamentSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

    def put(self, request: WSGIRequest):
        serializer = DepartamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentDetail(APIView):
    def get_object(self, pk: int):
        try:
            return DepartamentModel.objects.get(pk=pk)
        except DepartamentModel.DoesNotExist:
            raise Http404

    def get(self, request: WSGIRequest, pk: int):
        departament = self.get_object(pk)
        serializer = DepartamentSerializer(departament)
        return Response(serializer.data)

    def put(self, request: WSGIRequest, pk: int):
        departament = self.get_object(pk)
        serializer = DepartamentSerializer(departament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: WSGIRequest, pk: int):
        departament = self.get_object(pk)
        name = departament.name
        departament.delete()
        return Response({"detail": f"OK. Departament '{name}' was deleted."})