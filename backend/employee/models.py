from django.db import models

# Create your models here.
class Employee(models.Model):
       
    emp_name=models.CharField(max_length=64)
    emp_id=models.CharField(max_length=64)
    emp_email=models.EmailField(max_length=128)
    
    manager_name=models.CharField(max_length=64, null=True,blank=True)
    manager_id=models.CharField(max_length=64, null=True,blank=True)
    manager_email=models.EmailField(max_length=128, null=True,blank=True)
    current_role=models.CharField(max_length=64) # "coder"
    past_roles=models.CharField(max_length=512) # "coder, developer, janator" (seperator: ,)
    effective_date = models.DateTimeField(null=True,blank=True)
    Expiration_date = models.DateTimeField(null=True,blank=True)
    desk_location=models.CharField(max_length=64)

    def __str__(self):
        return self.emp_name