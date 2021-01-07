from rest_framework.views import APIView, Response
import re
from employee.models import EmployeeDetails
from employee.serializers import EmployeeDetailsSerializer


class DeleteEmployeeDetailsAPI(APIView):
    """This covers the API for delete employee details."""
    def post(self, request):
        input_data, output_data, employee_details_data = request.data["APIData"], {}, {}
        output_data = dict(zip(['Payload'], [None]))
        try:
            employee_details_data = self.delete_employee_records(input_data)
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

    def delete_employee_records(self, input_data):
        """this function is used to delete records from employee details tables"""
        try:
            check_emp_id = EmployeeDetails.objects.get(pk=input_data['employee_id'])
            check_emp_id.delete()
            output_data = dict(zip(['Status', 'Message'], ['Success', "Successfully employee data is deleted"]))
            return output_data
        except Exception as ex:
            output_data = dict(zip(['Status', 'Message', 'Payload'],
                                   ['Failure', f"Issue happening while updating data:{ex}", None]))
            return output_data

