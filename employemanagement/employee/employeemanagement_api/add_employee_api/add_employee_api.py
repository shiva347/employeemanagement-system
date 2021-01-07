from rest_framework.views import APIView, Response
import re
from employee.models import EmployeeDetails
from employee.serializers import EmployeeDetailsSerializer


class AddEmployeeDetailsAPI(APIView):
    """This covers the API for add employee details."""
    def post(self, request):
        input_data, output_data, employee_details_data = request.data["APIData"], {}, {}
        output_data = dict(zip(['Payload'], [None]))
        try:
            employee_details_data = self.add_employee_records(input_data)
            check = re.findall(r"'Status': 'Failure'", str(employee_details_data))
            if check:
                output_data['Payload'] = employee_details_data
                return Response(output_data)
            output_data['Payload'] = employee_details_data['Payload']
            return Response(output_data)

        except Exception as ex:
            output_data['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ["Failure",
                                                                                 f"Something having internal issue."
                                                                                 f" at fetching payload: {ex}.",
                                                                                 employee_details_data['Payload']]))
            return Response(output_data)

    def add_employee_records(self,request):
        """this function is responsible for add new employee details"""
        input_data, output_data = request, {}
        try:
            # this function is used for check employee from our db
            employee_check = self.check_employee_existence(input_data)
            if employee_check['Status'] == 'Failure':
                return employee_check
            else:
                # create employee details
                add_employee = self.insert_employee_records(input_data)
                output_data = dict(zip(['Status', 'Message', 'Payload'],
                                       ['Success', f"Successfully employee added. ", add_employee]))
                return output_data
        except Exception as ex:
            output_data = dict(zip(['Status', 'Message'],
                                   ['Failure', f"Issues happened while fetching employee details. "
                                               f"Encountered Exception: {ex} "]))
            return output_data

    def check_employee_existence(self, request):
        input_data, output_data = request, {}
        """ this function is check employee details from email_id """
        try:
            check_emp_id = EmployeeDetails.objects.get(email_id=input_data['email_id']).employee_id
            output_data = dict(zip(['Status', 'Message', 'employee_id'],
                                   ['Failure', f"Employee is already register with this email_id.", check_emp_id]))
            return output_data

        except Exception as ex:
            output_data = dict(zip(['Status', 'Message'], ['Error', f"Employee not found: {ex} "]))
            return output_data

    def insert_employee_records(self, input_data):
        """this function is used to insert new records in our EmployeeDetails table"""
        try:
            employee_details = {}
            employee_details['email_id'] = input_data['email_id']
            employee_details['employee_name'] = input_data['full_name']
            employee_details['emp_location'] = input_data['location']
            serializer_data = EmployeeDetailsSerializer(data=employee_details)
            if serializer_data.is_valid(raise_exception=True):
                serializer_data.save()
                output_data = dict(zip(['Status', 'Message'], ['Success', "Successfully employee is added"]))
                return output_data
        except Exception as ex:
            output_data = dict(zip(['Status', 'Message', 'Payload'],
                                   ['Failure', f"Issue happening in data insertion:{ex}", None]))
            return output_data

