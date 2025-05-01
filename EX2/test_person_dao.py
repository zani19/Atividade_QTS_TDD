import unittest
from app import Email, Person, PersonDAO

class TestPersonDAO(unittest.TestCase):
    # Teste para nome válido
    def test_nome_valido(self):
        person = Person(1, "João Silva", 30, [Email(1, "joao@email.com")])
        self.assertEqual(PersonDAO.is_valid_to_include(person), [])

    # Teste para nome inválido (menos de duas partes)
    def test_nome_invalido_menos_de_duas_partes(self):
        person = Person(1, "João", 30, [Email(1, "joao@email.com")])
        self.assertIn("Nome deve conter ao menos duas partes e apenas letras", PersonDAO.is_valid_to_include(person))

    # Teste para nome inválido (caracteres não permitidos)
    def test_nome_invalido_caracteres(self):
        person = Person(1, "João123 Silva", 30, [Email(1, "joao@email.com")])
        self.assertIn("Nome deve conter ao menos duas partes e apenas letras", PersonDAO.is_valid_to_include(person))

    # Teste para idade válida
    def test_idade_valida(self):
        person = Person(1, "João Silva", 30, [Email(1, "joao@email.com")])
        self.assertEqual(PersonDAO.is_valid_to_include(person), [])

    # Teste para idade inválida (menor que 1)
    def test_idade_invalida_menor_que_um(self):
        person = Person(1, "João Silva", 0, [Email(1, "joao@email.com")])
        self.assertIn("Idade deve estar entre 1 e 200", PersonDAO.is_valid_to_include(person))

    # Teste para idade inválida (maior que 200)
    def test_idade_invalida_maior_que_duzentos(self):
        person = Person(1, "João Silva", 201, [Email(1, "joao@email.com")])
        self.assertIn("Idade deve estar entre 1 e 200", PersonDAO.is_valid_to_include(person))

    # Teste para email válido
    def test_email_valido(self):
        person = Person(1, "João Silva", 30, [Email(1, "joao@email.com")])
        self.assertEqual(PersonDAO.is_valid_to_include(person), [])

    # Teste para email inválido
    def test_email_invalido(self):
        person = Person(1, "João Silva", 30, [Email(1, "joaoemail.com")])
        self.assertIn("Email inválido: joaoemail.com", PersonDAO.is_valid_to_include(person))

    # Teste para pessoa sem emails
    def test_sem_emails(self):
        person = Person(1, "João Silva", 30, [])
        self.assertIn("Pessoa deve ter ao menos um email", PersonDAO.is_valid_to_include(person))

if __name__ == "__main__":
    unittest.main()