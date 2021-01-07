"""
this is get api call
it returns all data from db

when no any records in our db

http method= GET
APIResponse:-

[
    {
        "employee_id": 14,
        "email_id": "shiva1@gmail.com",
        "employee_name": "Shiva"
    },
    {
        "employee_id": 15,
        "email_id": "shiva11@gmail.com",
        "employee_name": "Shiva"
    }
]

# when no any response found
{
    "Payload": {
        "Status": "Success",
        "Message": "looks like no any employee yet.",
        "Payload": []
    }
}
"""