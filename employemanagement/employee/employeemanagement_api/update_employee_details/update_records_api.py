from rest_framework.views import APIView, Response
import re
from employee.models import EmployeeDetails
from employee.serializers import EmployeeDetailsSerializer


class UpdateEmployeeDetailsAPI(APIView):
    """This covers the API for update employee details."""
    def post(self, request):
        input_data, output_data, employee_details_data = request.data["APIData"], {}, {}
        output_data = dict(zip(['Payload'], [None]))
        try:
            employee_details_data = self.update_employee_records(input_data)
            check = re.findall(r"'Status': 'Failure'", str(employee_details_data))
            if check:
                output_data['Payload'] = employee_details_data
                return Response(output_data)
            output_data['Payload'] = employee_details_data
            return Response(output_data)

        except Exception as ex:
            output_data['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ["Failure",
                                                                                 f"Something having internal issue."
                                                                                 f" at fetching payload: {ex}.",
                                                                                 employee_details_data['Payload']]))
            return Response(output_data)

    def update_employee_records(self, input_data):
        """this function is used to update  records in our EmployeeDetails table"""
        try:
            check_emp_id = EmployeeDetails.objects.get(employee_id=input_data['employee_id'])
            check_emp_id.emp_location = input_data['update_location']
            check_emp_id.save()
            output_data = dict(zip(['Status', 'Message'], ['Success', "Successfully employee data is updated"]))
            return output_data
        except Exception as ex:
            output_data = dict(zip(['Status', 'Message', 'Payload'],
                                   ['Failure', f"Issue happening while updating data:{ex}", None]))
            return output_data

