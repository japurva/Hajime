from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from employee.models import Employee
from django.utils import timezone
from datetime import datetime
from django.utils.translation import gettext as _

# Create your models here.

class Attendance(models.Model):
	employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
	checkin = models.TimeField(_(u"CheckIn Time"), blank=True)
	checkout = models.TimeField(_(u"CheckOut Time"), blank=True)
	totalhours = models.DecimalField(max_digits=4, decimal_places=2)
	status = models.CharField(max_length=12,default='pending') #pending,approved,rejected,cancelled
	attendancefor = models.DateTimeField(auto_now=True, auto_now_add=False)  
	remarks = models.CharField(max_length=120, null=True)
	is_approved = models.BooleanField(default=False) #hid

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)



	class Meta:
		verbose_name = ('Attendance')
		verbose_name_plural = ('Attendance')
		ordering = ['-created'] #recent objects

	def __str__(self):
		return str(self.employee)
