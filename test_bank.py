from bank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Given
        entrada = "13/03/2000"
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1111)

        # When
        resultado = funcionario_teste.idade()

        # Then
        assert resultado == esperado

    def test_quando_nome_Victor_Hugo_Silva_deve_retornar_Silva(self):
        # Given
        entrada = "Victor Hugo Silva"
        esperado = "Silva"

        funcionario_teste = Funcionario(entrada, "04/07/2002", 1000000)

        # When
        resultado = funcionario_teste.sobrenome()

        # Then
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/1111", entrada_salario)

        # When
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given
        entrada_salario = 1000
        esperado = 100.0

        funcionario_teste = Funcionario(
            "Ana Machado da Silva", "11/11/1111", entrada_salario
        )

        # When
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            # Given
            entrada_salario = 1000000

            funcionario_teste = Funcionario(
                "Ana Machado da Silva", "11/11/1111", entrada_salario
            )

            # When
            resultado = funcionario_teste.calcular_bonus()

            # Then
            assert resultado

    # def test_retorno_dunder_str(self):
    #     # Given
    #     nome, data_nascimento, salario = "Paulo Alves Lima", "13/03/2000", 1200
    #     esperado = "Funcionario(Paulo Alves Lima, 13/03/2000, 1200)"

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)

    #     # When
    #     resultado = funcionario_teste.__str__()

    #     # Then
    #     assert resultado == esperado
