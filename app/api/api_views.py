from django.core.handlers.wsgi import WSGIRequest
from django.core.serializers import serialize
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response

from .base import BaseList, BaseDetail
from app.models import (
    DepartamentModel, PositionModel, PermissionModel, EmployeeModel
)
from .serializers import (
    DepartamentSerializer, PositionSerializer, PermissionSerializer, EmployeeSerializer
)


class DepartamentList(BaseList):
    def __init__(self, **kwargs):
        super().__init__(DepartamentModel, DepartamentSerializer, **kwargs)

class DepartamentDetail(BaseDetail):
    def __init__(self, **kwargs):
        super().__init__(DepartamentModel, DepartamentSerializer, **kwargs)

class PositionList(BaseList):
    def __init__(self, **kwargs):
        super().__init__(PositionModel, PositionSerializer, **kwargs)

class PositionDetail(BaseDetail):
    def __init__(self, **kwargs):
        super().__init__(PositionModel, PositionSerializer, **kwargs)

class PermissionList(BaseList):
    def __init__(self, **kwargs):
        super().__init__(PermissionModel, PermissionSerializer, **kwargs)

class PermissionDetail(BaseDetail):
    def __init__(self, **kwargs):
        super().__init__(PermissionModel, PermissionSerializer, **kwargs)

class EmployeeList(BaseList):
    def __init__(self, **kwargs):
        super().__init__(EmployeeModel, EmployeeSerializer, **kwargs)

class EmployeeDetail(BaseDetail):
    def __init__(self, **kwargs):
        super().__init__(EmployeeModel, EmployeeSerializer, **kwargs)

    @staticmethod
    def extend(employee: EmployeeModel, data: dict) -> dict:
        extra_departament = {
            "name": employee.departament.name,
        }
        data["departament"] = extra_departament

        extra_position = [{
            "name": position.name,
            "salary": position.salary,
        } for position in employee.position.all()]
        data["position"] = extra_position

        extra_permission = [{
            "name": permission.name,
            "description": permission.description,
            "code": permission.code,
        } for permission in employee.permissions.all()]
        data["permissions"] = extra_permission

        return data

    def get(self, request: WSGIRequest, pk: int):
        employee = self.get_object(pk)
        serializer = self.serializer(employee)
        data = self.extend(employee, serializer.data)
        return Response(data)
