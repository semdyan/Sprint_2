class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.employee_salary = hours * self.hourly_payment

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        self.employee_salary = self.hours * self.hourly_payment
        return self.employee_salary


emp = EmployeeSalary('dsa', 22, 1, 'da')
print(emp.employee_salary)
emp.hours = 1
emp.salary()
print(emp.__dict__)
print(emp.employee_salary) 