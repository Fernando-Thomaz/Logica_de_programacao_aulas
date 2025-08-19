'''
Programa: adivinha V.1.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema adivinha o numero
'''
from random import randint

print(f"Tente adivinha o numero!")
n1 = int(input(f"Digite um numero entre 1 e 10: "))

n_sec = randint(1,10)

if n1 == n_sec:
    print(f"Parabens!!!\nVocê ganhou!!\nSeu numero: {n1}\nNumero secreto: {n_sec}")
else:
    print(f"Você errou\nSeu numero: {n1}\nNumero secreto: {n_sec}")