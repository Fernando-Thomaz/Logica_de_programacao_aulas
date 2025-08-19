'''
Programa: sorteio V.1.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema recebe o nome dos candidatos e realiza o sorteio
'''
import random

lista = []

sair = False

while sair == False:
    candidato = str(input(f"Digite os nomes para o sorteio ou pressione enter para sair: "))
    if candidato != "":
        #APPEND e para adicionar uma variavel a lista
        lista.append(candidato)
    else:
        sair = True
escolhido = random.choices(lista)
print(f"Escolhido foi: {escolhido}")