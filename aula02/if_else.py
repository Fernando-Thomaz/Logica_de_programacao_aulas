'''
concatenação
quebra de linha
formatando decimais
alterando virgula e ponto
if else
operadores ternario
'''
#entrada de dados
nome = str(input(f"Qual é seu nome? "))
idade = int(input(f"Quantos anos você tem? "))
peso = float(input("Digite o seu peso: ").replace(",","."))#entrada de dados tratando o "," como um "."
altura = float(input("Digite o seu altura: ").replace(",","."))#entrada de dados tratando o "," como um "." 

#NOTE - concatenação com +

#quebra de linha
print(40*"-")

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

#quebra de linha
print(40*"-")

#colocando duas linhas de codigo em uma linha de saida de dados
print(f"O sábio sabia ", end="")
print(f"que sabiá sabia assobiar.")

#NOTE - limitando quantidade de casas depois da virgula

#quebra de linha
print(40*"-")

#dados com muitos números depois da virgula
valor = 1.23456789

#exibindo o valor sem limitar casas
print(f"{valor}")

#exibindo apenas duas casas depois da virgula
print(f"{valor:.2f}")

#quebra de linha
print(40*"-")

#NOTE - tratar virgula como ponto

#mostrando na tela
print(f"Seu peso é {peso:.2f}".replace(".",","))#saida de dados tratando o "." como ","

#NOTE - if else

#quebra de linha
print(40*"-")

if idade >= 18:
    print(f"{nome} é maior de idade.")
    print(f"Você esta dentro do bloco do if.")

else:
    print(f"{nome} é menor de idade.")
    print(f"Você esta dentro do bloco do else.")