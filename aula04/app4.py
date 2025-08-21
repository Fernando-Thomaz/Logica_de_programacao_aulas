'''
Programa: sorteio V.3.0
Importando biblioteca
Random: escolha aleatoria
Descrição sistema recebe o nome dos candidatos e realiza o sorteio
'''
import random
import os
import time

lista_nome = []
lista_sorteio = []

while True:
    nome = input("Digite o nome para o sorteio: ")
    if nome:
        lista_nome.append(nome)
    else:
        break

while True:
    if lista_nome:
        os.system("cls")
        escolhido = random.choice(lista_nome)
        lista_sorteio.append(escolhido)
        #exclui o sorteio da lista original
        '''
        pop - função, remove pelo indice
            pop() - remove o ultimo elemento adicionado
            pop(0) - remove o indice selecionado
        del - instrucao, remover item pelo indice, mais de um item
            del[1::10]
        remove - remove a partir de uma variavel
            lista.remove(variavel)
        '''
        print(f"O escolhido foi: {escolhido}")
        lista_nome.remove(escolhido)

        opcao = input(f"Deseja sortear outro nome?\nS - sim | N - não\n").lower()
        os.system("cls")

        if opcao == "s":
            continue
        else:
            break
    else:
        print(f"Não há nomes para serem sorteados")
        break
print(f"Programa finalizado!")
print(f"Os sorteados foram {lista_sorteio}")