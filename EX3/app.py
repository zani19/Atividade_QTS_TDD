class Employee:
    def __init__(self, name: str, email: str, base_salary: float, role: str):
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.role = role

class SalaryCalculator:
    @staticmethod
    def calculate_net_salary(employee: Employee) -> float:
        if employee.role == "DESENVOLVEDOR":
            if employee.base_salary >= 3000:
                return employee.base_salary * 0.8
            else:
                return employee.base_salary * 0.9
        elif employee.role == "DBA" or employee.role == "TESTADOR":
            if employee.base_salary >= 2000:
                return employee.base_salary * 0.75
            else:
                return employee.base_salary * 0.85
        elif employee.role == "GERENTE":
            if employee.base_salary >= 5000:
                return employee.base_salary * 0.7
            else:
                return employee.base_salary * 0.8
        else:
            raise ValueError("Cargo inválido")