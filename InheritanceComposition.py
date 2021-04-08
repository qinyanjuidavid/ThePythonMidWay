class PayrollSystem(object):
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id}- {employee.name}")
            print(f"-Check amount: {employee.calculate_payroll()}")
            print('')

class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=names

class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly_salary):
        super().__init__(id,name)
        self.weekly_salary=weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary
    