"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada
em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode
ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir
qual interruptor controla qual lâmpada. Como você faria para descobrir, usando
apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada
lâmpada?

Resposta:
Passo 1 - Ligue o primeiro interruptor (A) e deixe ligado por alguns minutos.
Isso fará com que a lâmpada conectada a ele esquente.
Passo 2 - Desligue o interruptor A.
Passo 3 - Ligue o segundo interruptor (B) e vá para a sala das lâmpadas:
    Lâmpada acesa: A lâmpada que está acesa está conectada ao interruptor B.
    Lâmpada apagada e quente: A lâmpada que está apagada, mas ainda quente, está
    conectada ao interruptor A (que você deixou ligado por um tempo e depois
    desligou).
    Lâmpada apagada e fria: A lâmpada que está apagada e fria está conectada ao
    interruptor C (que você nunca ligou).
Passo 4 - Agora você sabe qual interruptor controla cada lâmpada:
    A lâmpada acesa é controlada pelo interruptor B.
    A lâmpada quente é controlada pelo interruptor A.
    A lâmpada fria é controlada pelo interruptor C.
"""
