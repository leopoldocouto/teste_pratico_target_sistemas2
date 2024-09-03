from teste_pratico_target_sistemas2.questao2 import questao2

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_comparar_true_para_quantidade_a() -> None:
    string: str = 'Target Sistemas'
    quest3: int = questao2(string)
    resp3: int = 2
    assert quest3 == resp3


def test_deve_comparar_true_para_quantidade_zero() -> None:
    string: str = 'Leopoldo Couto'
    quest3: int = questao2(string)
    resp3: int = 0
    assert quest3 == resp3


def test_deve_comparar_true_para_parametro_errado() -> None:
    string = 123
    quest3: int = questao2(string)
    resp3: int = -1
    assert quest3 == resp3
