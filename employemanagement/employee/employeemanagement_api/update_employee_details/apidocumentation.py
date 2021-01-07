"""
Note:
1. here i take employee_id from user / because here i not implementing login so we not get any kind of user data
if user is login then i get user_id so which is map with employeedetails table on the based i update the details
and i ony changes employee_location because in employee details every thing is mostly fixed but we can update any field

htpp method: -POST
APIData:-
{
    "APIData":{
        "employee_id":25,
        "update_location" : "Madhubani"


    }
}
APIResponse:-

{
    "Payload": {
        "Status": "Success",
        "Message": "Successfully employee data is updated"
    }
}
"""