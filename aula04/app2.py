'''
Programa: sorteio V.1.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema recebe o nome dos candidatos e realiza o sorteio
'''
import random

n1 = str(input(f"Digite o primeiro nome: "))
n2 = str(input(f"Digite o segundo nome: "))
n3 = str(input(f"Digite o terceiro nome: "))
n4 = str(input(f"Digite o quarto nome: "))
n5 = str(input(f"Digite o quinto nome: "))

lista = [n1,n2,n3,n4,n5]

escolhido = random.choice(lista)
print(escolhido)