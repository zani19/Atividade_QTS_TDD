# Atividade_QTS_TDD
Repositorio destinado a atividade prática de TDD

Como Rodar o Sistema:

1. Certifique-se de que o Python está instalado no sistema. Para verificar, execute o comando:
   python --version

2. Navegue até o diretório onde o projeto está localizado.

3. Para executar os testes do exercício 1 (classificação de triângulos), utilize o seguinte comando:
   cd "EX1"
   python -m unittest test_triangle.py

4. Para executar os testes do exercício 2 (validação de pessoas e emails), utilize o seguinte comando:
   cd "../EX2"
   python -m unittest test_person_dao.py

5. Para executar os testes do exercício 3 (calculadora de salário de funcionários), utilize o seguinte comando:
   cd "../EX3"
   python -m unittest test_salary_calculator.py

6. Se desejar uma saída mais detalhada dos testes, utilize o comando:
   python -m unittest -v test_triangle.py  # Para o exercício 1
   python -m unittest -v test_person_dao.py  # Para o exercício 2
   python -m unittest -v test_salary_calculator.py  # Para o exercício 3

7. Verifique os resultados no terminal. Se todos os testes passarem, a mensagem "OK" será exibida.