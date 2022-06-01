import imp
from django.contrib import admin
from .models import Employee


# Register your models here.

class EmployeeManager(admin.ModelAdmin):
    list_display = ['emp_id','emp_name','emp_email', 'current_role',
                    'manager_id','manager_name','manager_email',
                    'effective_date']


admin.site.register(Employee, EmployeeManager)