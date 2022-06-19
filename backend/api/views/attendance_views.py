from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from api.serializers.AttendanceSerializer import AttendanceSerializer
from attendance.models import Attendance

class AttendanceViewSet(viewsets.ModelViewSet):
    """
    View set which has add, edit, view, and list functionalities
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    model = Attendance
