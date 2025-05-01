import re

class Email:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Person:
    def __init__(self, id: int, name: str, age: int, emails: list[Email]):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails

class PersonDAO:
    @staticmethod
    def is_valid_to_include(p: Person) -> list[str]:
        errors = []

        # Nome: 2 partes e apenas letras
        name_parts = p.name.strip().split()
        if len(name_parts) < 2 or not re.match(r'^[A-Za-zÀ-ÿ\s]+$', p.name):
            errors.append('Nome deve conter ao menos duas partes e apenas letras')

        # Idade
        if p.age < 1 or p.age > 200:
            errors.append('Idade deve estar entre 1 e 200')

        # Emails
        if not p.emails or len(p.emails) == 0:
            errors.append('Pessoa deve ter ao menos um email')
        else:
            for email in p.emails:
                if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email.name):
                    errors.append(f'Email inválido: {email.name}')

        return errors