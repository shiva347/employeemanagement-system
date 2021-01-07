"""
API Documentations
First i want to mention : i have used only one model in our application to perform CRUD operation on employee
for more scalable used UUID user to create unique user, for location use Country, State,City and map in our table with
city_id , and UUID:

Alg:
Step1: check employee is registered with email_id or not
step2: if employee is registered then return failure message and employee id
step3: if employee is not registered insert new employee record in EmployeeDetails table

If you want to check use this in postman:-
http method : POST
select the json format:
{
    "APIData":{
        "email_id":"sk7@gmail.com",
        "full_name": "Shiva",
        "location": "kanhauli"

    }
}

APIResponse:-
{
    "Payload": {
        "Status": "Success",
        "Message": "Successfully employee is added"
    }
}


#for duplicate entry:
{
    "Payload": {
        "Status": "Failure",
        "Message": "Employee is already register with this email_id.",
        "employee_id": 14
    }
}
"""
