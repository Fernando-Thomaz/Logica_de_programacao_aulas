# bibliotecas
import random

# titulo
print(30*'-','LISTA DOBRADA','-'*30)

# cria uma lista com 10 numeros aleatorios entre 1 e 10
lista = [random.randint(1,10) for i in range(10)]
print(f'Lista original: {lista}')

# cria uma nova lista com o dobro dos valores da lista original
lista_dobrada = [x*2 for x in lista]

# mostra a nova lista
print(f'Lista dobrada: {lista_dobrada}')