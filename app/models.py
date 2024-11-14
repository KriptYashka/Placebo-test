from django.db import models

class DepartamentModel(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey("DepartamentModel", on_delete=models.SET_NULL, null=True, blank=True)

class PositionModel(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()


class PermissionModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    code = models.IntegerField()  # Права в числовом представлении


class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    # Примечание: я бы делал CASCADE, но работника ещё уволить надо без департамента и в системе должен находиться
    departament = models.ForeignKey(DepartamentModel, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ManyToManyField(PositionModel)
    permissions = models.ManyToManyField(PermissionModel)
