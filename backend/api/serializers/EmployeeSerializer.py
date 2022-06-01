from employee.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields=['emp_id','emp_name','emp_email', 'current_role',]
