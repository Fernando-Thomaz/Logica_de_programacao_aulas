'''
concatenação
quebra de linha
formatando decimais
alterando virgula e ponto
if else
operadores ternario
'''
'''
#entrada de dados
nome = str(input(f"Qual é seu nome? ").upper())
idade = int(input(f"Quantos anos você tem? "))
peso = float(input("Digite o seu peso: ").replace(",","."))#entrada de dados tratando o "," como um "."
altura = float(input("Digite o seu altura: ").replace(",","."))#entrada de dados tratando o "," como um "." 

#NOTE - concatenação com +

#quebra de linha
print(60*"-")

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
print(60*"-")

#colocando duas linhas de codigo em uma linha de saida de dados
print(f"O sábio sabia ", end="")
print(f"que sabiá sabia assobiar.")

#NOTE - limitando quantidade de casas depois da virgula

#quebra de linha
print(60*"-")

#dados com muitos números depois da virgula
valor = 1.23456789

#exibindo o valor sem limitar casas
print(f"{valor}")

#exibindo apenas duas casas depois da virgula
print(f"{valor:.2f}")

#quebra de linha
print(60*"-")

#NOTE - tratar virgula como ponto

#mostrando na tela
print(f"Seu peso é {peso:.2f}".replace(".",","))#saida de dados tratando o "." como ","

#NOTE - if else

#quebra de linha
print(60*"-")

if idade >= 18:
    print(f"{nome} é maior de idade.")
    print(f"Você esta dentro do bloco do if.")

else:
    print(f"{nome} é menor de idade.")
    print(f"Você esta dentro do bloco do else.")

#entrada de dados
n1 = int(input(f"Escolha um número qualquer: "))

#codição para ver se o numero é impar ou par
if n1 %2 == 0:
    print(f"Número par.")
else:
    print(f"Número impar.")

#titulo
print(30*"-","Boletim escolar",30*"-")

#entrada de nome
nome2 = str(input("Digite o nome do aluno: ").upper())#upper = maiusculo /lower =minusculo

#entrada das notas
nota1 = float(input("Digite a primeira nota: ").replace(",","."))
nota2 = float(input("Digite a segunda nota: ").replace(",","."))
nota3 = float(input("Digite a terceira nota: ").replace(",","."))
nota4 = float(input("Digite a quarta nota: ").replace(",","."))

#soma da media
media = (nota1+nota2+nota3+nota4)/4
'''
'''
verificando se passou
 >= 7: aprovado
 >= 5: recuperação
 reprovado
'''
'''
#nome do aluno na tela
print(f"Nome do aluno: {nome2}")

if media >= 7:
    print(f"Sua media: {media:.2f}, você passou".replace(".",","))
    print(f"Nota 1: {nota1} | Nota 2: {nota2}".replace(".",","))
    print(f"Nota 3: {nota3} | Nota 4: {nota4}".replace(".",","))

elif media >= 5:
    print(f"Sua media: {media:.2f}, você ficou de recuperação".replace(".",","))
    print(f"Nota 1: {nota1} | Nota 2: {nota2}".replace(".",","))
    print(f"Nota 3: {nota3} | Nota 4: {nota4}".replace(".",","))

else:
    print(f"Sua media: {media:.2f}, você reprovou".replace(".",","))
    print(f"Nota 1: {nota1} | Nota 2: {nota2}".replace(".",","))
    print(f"Nota 3: {nota3} | Nota 4: {nota4}".replace(".",","))

#titulo
print(30*"-","Entrada do parque",30*"-")

#entrada de dados
nome3 = str(input("Qual é o seu nome? ").upper())
idade2 = int(input("Quantos anos você tem? "))
altura2 = float(input("Qual a sua altura? ").replace(",","."))

#verifica se o usuario possui os requisitos minimos
if idade2 >= 12 and altura2 >= 1.2:
    print(f"A entrada de {nome3} é permitida.")

else:
    print(f"A entrada de {nome3} não é permitida")
'''
'''
#titulo
print(30*"-","Menor ou maior de idade",30*"-")

#entrada de dados
nome4 = str(input("Escreva o seu nome: ").upper())
idade3 = int(input("Escreva a sua idade: "))

#operarios ternario
print(f"{nome4} é maior de idade" if idade3 >= 18 else f"{nome4} é menor de idade")
'''