from rest_framework.decorators import authentication_classes

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
