import imp
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers.EmployeeSerializer import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    VtJob View set which has add, edit, view, and list functionalities
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    model = Employee
