from pydantic_models import Employee

employee = Employee(
    name="Chris DeTuma",
    email="cdetuma@example.com",
    date_of_birth="1998-04-02",
    salary=123_000.00,
    department="IT",
    elected_benefits=True,
)

json_employee = employee.json()
print(json_employee)
