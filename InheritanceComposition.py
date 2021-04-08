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
class HourlyEmployee(Employee):
    def __init__(self,id,name,hours_worked,hour_rate):
        super().__init__(id,name)
        self.hours_worked=hours_worked
        self.hour_rate=hour_rate
    def calculate_payroll(self):
        return self.hours_worked*self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self,id,name,weekly_salary,commission):
        super().__init__(id,name,weekly_salary)
        self.commission=commission
    def calculate_payroll(self):
        fixed=super().calculate_payroll()
        return fixed+self.commission
