from django.db import models

# Create your models here.

# As a mention in interview employee have 4 data
# this models based on only purpose CRUD operation, for more scalable need to be make more table, like Company, Location


class EmployeeDetails(models.Model):
    employee_id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=100, default=None)
    employee_name = models.CharField(max_length=100, default=None)
    emp_location = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.employee_id)

