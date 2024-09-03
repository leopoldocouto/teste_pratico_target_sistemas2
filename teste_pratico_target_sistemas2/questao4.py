"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

Respostas:

# Sequência de números ímpares elevados ao quadrado
a) 1, 3, 5, 7, [9]
# Sequência de números pares elevados ao quadrado
b) 2, 4, 8, 16, 32, 64, [128]
# Sequência de quadrados perfeitos
c) 0, 1, 4, 9, 16, 25, 36, [49]
# Sequência de quadrados de números pares
d) 4, 16, 36, 64, [100]
# Sequência de Fibonacci
e) 1, 1, 2, 3, 5, 8, [13]
# Sequência mista de números ímpares e pares
f) 2, 10, 12, 16, 17, 18, 19, [20]
"""

type_dict = dict[str, int]


def questao4() -> type_dict:
    sequencias: dict[str, list[int]] = {
        'a': [1, 3, 5, 7],
        'b': [2, 4, 8, 16, 32, 64],
        'c': [0, 1, 4, 9, 16, 25, 36],
        'd': [4, 16, 36, 64],
        'e': [1, 1, 2, 3, 5, 8],
        'f': [2, 10, 12, 16, 17, 18, 19],
    }
    respostas: type_dict = {}
    # a) Sequência de números ímpares
    respostas['a'] = sequencias['a'][-1] + 2
    # b) Sequência de potências de 2
    respostas['b'] = sequencias['b'][-1] * 2
    # c) Sequência de quadrados perfeitos
    n = len(sequencias['c'])  # O próximo n é igual a len(sequencias['c'])
    respostas['c'] = n**2
    # d) Sequência de quadrados de números pares
    n = len(sequencias['d']) * 2 + 2
    respostas['d'] = n**2
    # e) Sequência de Fibonacci
    respostas['e'] = sequencias['e'][-1] + sequencias['e'][-2]
    # f) Sequência mista
    respostas['f'] = sequencias['f'][-1] + 1
    return respostas


# Exemplo de chamada da função
if __name__ == '__main__':
    resultados = questao4()
    for chave, valor in resultados.items():
        print(f'{chave}) {valor}')
