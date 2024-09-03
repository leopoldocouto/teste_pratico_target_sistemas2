from teste_pratico_target_sistemas2.questao3 import questao3

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert


def test_deve_comparar_true_para_resultado_correto_questao3() -> None:
    quest3: int = questao3()
    resp3: int = 77
    assert quest3 == resp3


def test_deve_diferenciar_true_para_resultado_errado_questao3() -> None:
    quest3: int = questao3()
    resp3: int = 78
    assert quest3 != resp3
