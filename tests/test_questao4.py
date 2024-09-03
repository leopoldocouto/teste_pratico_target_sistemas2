from teste_pratico_target_sistemas2.questao4 import questao4

# given (dado quem, cenário) Arrange
# when  (quando algo acontecer) Act
# then  (então algo deve ser verificado) Assert

type_dict = dict[str, int]


def test_deve_retornar_lista_reposta_questao4() -> None:
    quest4: type_dict = questao4()
    resp4: list[int] = [9, 128, 49, 100, 13, 20]
    assert list(quest4.values()) == resp4
