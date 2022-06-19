from attendance.models import Attendance
from rest_framework import serializers
#from api.serializers.EmployeeSerializer import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    #emp = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model=Attendance
        fields='__all__'
