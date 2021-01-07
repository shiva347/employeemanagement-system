from rest_framework.views import APIView, Response
from employee.models import EmployeeDetails
from django.http import JsonResponse


class GetAllEmployeeDetailsAPI(APIView):
    """This covers the API for get employee details from our db."""
    def get(self, request):
        output_data = dict(zip(['Payload'], [None]))
        try:
            employee_details = EmployeeDetails.objects.all().values('employee_id', 'email_id', 'employee_name')
            employee_list = list(employee_details)
            if len(employee_details) > 0:
                return JsonResponse(employee_list, safe=False)
            else:
                output_data['Payload'] = dict(zip(['Status', 'Message', 'Payload'],
                                                  ["Success", f"looks like no any employee yet.", employee_list]))
                return Response(output_data)

        except Exception as ex:
            output_data['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ["Failure",
                                                                                 f"Something having internal issue."
                                                                                 f" at fetching payload: {ex}."]))
            return Response(output_data)


