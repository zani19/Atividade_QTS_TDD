import unittest
from app import Triangle

class TestTriangle(unittest.TestCase):
    # Triângulo escaleno válido
    def test_escaleno_valido(self):
        self.assertEqual(Triangle.classify(3, 4, 5), "Escaleno")

    # Triângulo isósceles válido
    def test_isosceles_valido(self):
        self.assertEqual(Triangle.classify(5, 5, 3), "Isósceles")
        self.assertEqual(Triangle.classify(5, 3, 5), "Isósceles")
        self.assertEqual(Triangle.classify(3, 5, 5), "Isósceles")

    # Triângulo equilátero válido
    def test_equilatero_valido(self):
        self.assertEqual(Triangle.classify(6, 6, 6), "Equilátero")

    # Um valor zero
    def test_valor_zero(self):
        self.assertEqual(Triangle.classify(0, 4, 5), "Valores devem ser positivos")

    # Um valor negativo
    def test_valor_negativo(self):
        self.assertEqual(Triangle.classify(-3, 4, 5), "Valores devem ser positivos")

    # Soma de dois lados igual ao terceiro lado
    def test_soma_dois_lados_igual_terceiro(self):
        self.assertEqual(Triangle.classify(1, 2, 3), "Não forma triângulo")
        self.assertEqual(Triangle.classify(2, 3, 1), "Não forma triângulo")
        self.assertEqual(Triangle.classify(3, 1, 2), "Não forma triângulo")

    # Soma de dois lados menor que o terceiro lado
    def test_soma_dois_lados_menor_terceiro(self):
        self.assertEqual(Triangle.classify(1, 1, 3), "Não forma triângulo")
        self.assertEqual(Triangle.classify(1, 3, 1), "Não forma triângulo")
        self.assertEqual(Triangle.classify(3, 1, 1), "Não forma triângulo")

    # Todos os valores iguais a zero
    def test_todos_valores_zero(self):
        self.assertEqual(Triangle.classify(0, 0, 0), "Valores devem ser positivos")

if __name__ == "__main__":
    unittest.main()