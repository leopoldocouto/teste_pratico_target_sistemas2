"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela
ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua
preferência ou pode ser previamente definida no código;
"""


def questao2(string: str) -> int:
    if not isinstance(string, str):
        return -1
    string = string.lower()
    quantidade_a: int = string.count('a')
    return quantidade_a
