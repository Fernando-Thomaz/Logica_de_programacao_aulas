'''
Programa: sorteio V.2.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema recebe o nome dos candidatos e realiza o sorteio
'''
import random

lista = []

sair = False

while sair == False:
    candidato = str(input(f"Digite os nomes para o sorteio ou pressione enter para sair: "))
    if candidato == "":
        sair = True
    else:
        #APPEND e para adicionar uma variavel a lista
        lista.append(candidato)
escolhido = random.choice(lista)
print(f"Escolhido foi: {escolhido}")