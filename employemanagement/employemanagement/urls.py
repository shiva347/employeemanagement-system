"""employemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from employee.employeemanagement_api.add_employee_api.add_employee_api import AddEmployeeDetailsAPI
from employee.employeemanagement_api.get_allemployee_api.get_allemployee_api import GetAllEmployeeDetailsAPI
from employee.employeemanagement_api.update_employee_details.update_records_api import UpdateEmployeeDetailsAPI
from employee.employeemanagement_api.delete_employee_details.delete_employee_details_api import DeleteEmployeeDetailsAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^add_employee/$', AddEmployeeDetailsAPI.as_view()),
    url(r'^get_all_employee/$', GetAllEmployeeDetailsAPI.as_view()),
    url(r'^update_emp_details', UpdateEmployeeDetailsAPI.as_view()),
    url(r'^delete_emp_details', DeleteEmployeeDetailsAPI.as_view()),
]
