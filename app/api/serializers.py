from rest_framework import serializers

from app.models import DepartamentModel


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentModel
        fields = ["id", "name", "head"]