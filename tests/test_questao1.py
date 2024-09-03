from teste_pratico_target_sistemas2.questao1 import questao1

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_retornar_true_para_questao1() -> None:
    numero: int = 8
    quest1: bool = questao1(numero)
    resp1: bool = True
    assert quest1 == resp1


def test_deve_retornar_false_para_questao1() -> None:
    numero: int = 7
    quest1: bool = questao1(numero)
    resp1: bool = False
    assert quest1 == resp1
