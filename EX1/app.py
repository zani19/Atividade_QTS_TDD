class Triangle:
    @staticmethod
    def classify(a: int, b: int, c: int) -> str:
        if a <= 0 or b <= 0 or c <= 0:
            return "Valores devem ser positivos"

        if a + b <= c or a + c <= b or b + c <= a:
            return "Não forma triângulo"

        if a == b == c:
            return "Equilátero"
        if a == b or a == c or b == c:
            return "Isósceles"
        return "Escaleno"