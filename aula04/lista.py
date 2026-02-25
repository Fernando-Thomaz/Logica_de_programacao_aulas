'''
#NOTE - uma variavel pode ter mais de uma valor
lista = ["Fulano","Beltrano","Deltrano","Ciclano"]
#NOTE - se você printa sem definir qual o nome que você quer, ele vai mostrar todos
print(lista)
#mais se você definir o nome
print(lista[0])
print(lista[3])
#NOTE - FOR e para listar as variaveis composta 
#percorrer a lista
for nome in lista:
    print(nome)
#NOTE - RANGE é um tipo de lista que lista os numeros com alguns porem
#se você coloca uma informação, a informação e o fim da lista
#se você coloca duas e o inicio e o fim
#se você coloca tres e o inicio o fim e a quantidade de numero que ele pula de um para outro
for i in range(2,13,5):
    print(i)
#o LEN ele lista a numera as coisas dentro da lista
for i in range(len(lista)):
    print(i)
#NOTE - com o FOR ele muda o type conforme o pedido
tudo = ["Fer", 16, 1.5]
for n in tudo:
    print(n,type(n))
'''
'''
#NOTE - o IN com o IF é para verificar se o valor esta em uma lista
#Pedindo o nome
name = str(input("DIgite seu nome: "))
#verificando se o nome ta na lista
lista = ["Fulano","Fulano","Beltrano","Deltrano","Ciclano"]
if name in lista:
    print(name)
else:
    print(f"{name} não esta na lista")
#NOTE - o LEN pode ser substituido pelo .index()
#eles tem a mesma função de mostrar o numero da variavel
indice = lista.index(name)
#NOTE - o TRY ele trata uma exceções, então ele fala que se algo der errado tentar isso
#TRY alguma coisa, se nao der except
#nesse caso se o nome nao estiver no indice o codigo vai quebrar, entao se ele quebrar ele vai executar o outro codigo
try:
    print(f"{name} encontrado no {indice}")
except:
    print(f"{name} não esta na lista")
#NOTE - .count ele conta a quantidade de vezes que tem essa variavel
quantidade = lista.count(name)
try:
    print(f"{name} encontrado {quantidade} vezes")
except:
    print(f"{name} não esta na lista")
'''
'''
#NOTE - alterar um dado em uma lista
#agora na lista o numero 0 é fernando
lista1= ["Fulano","Fulano","Beltrano","Deltrano","Ciclano"]
print(lista1)
lista_altera = str(input("Informe o nome que desaja alterar: "))
lista1[lista1.index(lista_altera)] = str(input("Informe o novo nome: "))
for nom in lista1:
    print(nom)
'''
'''
#NOTE - tabuada
n1 = int(input(f"Tabuada de que número você quer saber: "))
#a tabuada vai ser definida por esse codigo
for i in range(1,11):
    resultado = n1 * i
    print(f"{i} X {n1} = {resultado}")
'''