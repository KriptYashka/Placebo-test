from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Avg, Max, Min
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.serializers import EmployeeListSerializer, DepartamentSerializer
from app.models import PositionModel, EmployeeModel, DepartamentModel


class PositionSalaryAvgView(APIView):
    def get(self, request: WSGIRequest):
        """
        Возвращает среднюю, максимальную и минимальную заработную плату
        """
        avg_salary, max_salary, min_salary = PositionModel.objects.aggregate(
            Avg("salary"), Max("salary"), Min("salary")
        ).values()
        data = {
            "avg": avg_salary,
            "max": max_salary,
            "min": min_salary,
        }
        return Response(data)

class DepartamentEmployeesView(APIView):
    def get(self, request: WSGIRequest, pk: int):
        """
        Возвращает информацию о депортаменте и её сотрудников
        """
        employees = EmployeeModel.objects.filter(departament__id=pk)
        try:
            departament = DepartamentModel.objects.get(pk=pk)
        except DepartamentModel.DoesNotExist:
            departament = None
        data = {
            "departament": departament,
            "employees": employees
        }
        serializer = EmployeeListSerializer(data)
        return Response(serializer.data)