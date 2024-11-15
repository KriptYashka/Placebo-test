from rest_framework import serializers
from app.models import DepartamentModel, PositionModel, PermissionModel, EmployeeModel


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentModel
        fields = ["id", "name", "head"]

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionModel
        fields = ["id", "name", "salary"]

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionModel
        fields = ["id", "name", "description", "code"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ["id", "name", "departament", "position", "permissions"]

class EmployeeExtendSerializer(serializers.Serializer):
    name = serializers.CharField()
    departament = DepartamentSerializer()
    position = PositionSerializer(many=True)
    permissions = PermissionSerializer(many=True)