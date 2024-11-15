from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseList(APIView):
    """
    Базовый класс представления API без передачи параметров в строке

    Используется для вывода всех объектов или добавления нового объекта
    """
    def __init__(self, model, serializer, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.serializer = serializer

    def get(self, request: WSGIRequest):
        queryset = self.model.objects.all()
        serializer_for_queryset = self.serializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

    def put(self, request: WSGIRequest):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseDetail(APIView):
    """
    Базовый класс представления API с передачей параметра pk в строке

    Используется для вывода, изменения и удаления одного объекта
    """
    def __init__(self, model, serializer, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.serializer = serializer

    def get_object(self, pk: int):
        """
        Возвращает объект из БД по ключу. Если объекта нет, то вызывает исключение *Http404*

        :raise Http404:
        """
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request: WSGIRequest, pk: int):
        """
        Информация об объекте
        """
        obj = self.get_object(pk)
        serializer = self.serializer(obj)
        return Response(serializer.data)

    def put(self, request: WSGIRequest, pk: int):
        """
        Обновление объекта
        """
        obj = self.get_object(pk)
        serializer = self.serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: WSGIRequest, pk: int):
        """
        Удаление объекта
        """
        obj = self.get_object(pk)
        obj.delete()
        return Response({"detail": f"OK"})
