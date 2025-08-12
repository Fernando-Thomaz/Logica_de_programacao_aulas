'''
concatenação
quebra de linha
formatando decimais
alterando virgula e ponto
if else
operadores ternario
'''

#dados
nome = "Fernando"
idade = 17
altura = 1.74

#NOTE - concatenação com +

#saida de dados
print("Olá, meu nome é " + nome + ", tenho " + str(idade) + " anos de idade")

#NOTE - concatenação com ,

#saida de dados
print("Olá, meu nome é",nome,", tenho",idade,"anos de idade")

#NOTE - concatenação com format

#saida de dados
print("Olá, meu nome é {}, tenho {} anos de idade".format(nome,idade))

#NOTE - concatenação com f-string

#saida de dados
print(f"Olá, meu nome é {nome}, tenho {idade} anos de idade")

#NOTE - eliminando quebra de linha

#colocando duas linhas de codigo em uma linha de saida de dados
print(f"O sábio sabia ", end="")
print(f"que sabiá sabia assobiar.")

#NOTE - limitando quantidade de casas depois da virgula

#dados com muitos números depois da virgula
valor = 1.23456789

#exibindo apenas duas casas depois da virgula
print(f"{valor:.2f}")

#quebra de linha
print(40*"-")

#NOTE - tratar virgula como ponto

#entrada de dados, trocando a virgula como ponto
peso = float(input("Digite o seu peso: ").replace(",","."))

#mostrando na tela
print(f"Seu peso é {peso:.2f}".replace(".",","))