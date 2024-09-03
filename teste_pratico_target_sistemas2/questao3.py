"""
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""


def questao3() -> int:
    indice: int = 12
    soma: int = 0
    k: int = 1
    while k < indice:
        k += 1
        soma += k
    return soma  # 77


questao3()
