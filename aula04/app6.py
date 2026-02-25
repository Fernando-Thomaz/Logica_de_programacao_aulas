'''
Programa: adivinha V.2.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema adivinha o numero
'''
import random
import os
import time

n_sec = random.randint(1,100)

tentativa = 0
max_tenta = 10
acertou = False

print(30*"-","Adivinha o número",30*"-")
print(f"Você tem {max_tenta} para adivinha o numero secreto, entre 1 e 100")

while tentativa <= max_tenta:
    try:
        n1 = int(input(f"Digite um numero:"))
    except ValueError:
        print(f"Por favor, digite um numero valido.")
        continue
    tentativa += 1
    if n1 == n_sec:
        acertou = True
        break
    elif n1 > n_sec:
        print("Tente um numero menor")  
        time.sleep(3)
        os.system("cls")
    else:
        print("Tente um numero maior")
        time.sleep(3)
        os.system("cls")
if acertou == False:
    print(f"Você perdeu\nNumero secreto: {n_sec}")
else:
    print(f"Parabens!!!\nVocê ganhou!!!\nSuas tentativas: {tentativa}\nNumero secreto: {n_sec}")