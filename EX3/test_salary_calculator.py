import unittest
from app import Employee, SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):
    # Teste para DESENVOLVEDOR com salário >= 3000
    def test_developer_salary_above_3000(self):
        employee = Employee("João", "joao@email.com", 3000, "DESENVOLVEDOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 2400)

    # Teste para DESENVOLVEDOR com salário < 3000
    def test_developer_salary_below_3000(self):
        employee = Employee("Maria", "maria@email.com", 2500, "DESENVOLVEDOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 2250)

    # Teste para DBA com salário >= 2000
    def test_dba_salary_above_2000(self):
        employee = Employee("Carlos", "carlos@email.com", 2000, "DBA")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1500)

    # Teste para DBA com salário < 2000
    def test_dba_salary_below_2000(self):
        employee = Employee("Ana", "ana@email.com", 1500, "DBA")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1275)

    # Teste para TESTADOR com salário >= 2000
    def test_tester_salary_above_2000(self):
        employee = Employee("Pedro", "pedro@email.com", 2500, "TESTADOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1875)

    # Teste para TESTADOR com salário < 2000
    def test_tester_salary_below_2000(self):
        employee = Employee("Clara", "clara@email.com", 1800, "TESTADOR")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 1530)

    # Teste para GERENTE com salário >= 5000
    def test_manager_salary_above_5000(self):
        employee = Employee("Roberto", "roberto@email.com", 5000, "GERENTE")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 3500)

    # Teste para GERENTE com salário < 5000
    def test_manager_salary_below_5000(self):
        employee = Employee("Fernanda", "fernanda@email.com", 4000, "GERENTE")
        self.assertEqual(SalaryCalculator.calculate_net_salary(employee), 3200)

    # Teste para cargo inválido
    def test_invalid_role(self):
        employee = Employee("Lucas", "lucas@email.com", 3000, "INVALIDO")
        with self.assertRaises(ValueError):
            SalaryCalculator.calculate_net_salary(employee)

if __name__ == "__main__":
    unittest.main()