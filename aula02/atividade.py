#NOTE - ATIVIDADE 1

#titulo
print(30*"-","ATIVIDADE 1",30*"-")

#variaveis
idade = 17
altura = 1.75
nome = "Fernando"
estudante = True

#mostrar valores
print(f"{idade}\n{altura}\n{nome}\n{estudante}")

#NOTE - ATIVIDADE 2

#titulo
print(30*"-","ATIVIDADE 2",30*"-")

#valores
n1 = 12
n2 = 7
n3 = 15
n4 = 4
n5 = 3
n6 = 2
soma = n1 + n2
resto = n2 % n4
potencia = n5 ** n6

print(f"O resultado de {n1} + {n2} é igual a {soma}")
print(f"O resultado de {n3} % {n4} é igual a {resto}")
print(f"O resultado de {n5} ** {n6} é igual a {potencia}")

#NOTE - ATIVIDADE 3

#titulo
print(30*"-","ATIVIDADE 3",30*"-")

#entrada de informações
nome = str(input("Qual é o seu nome? "))
print(f"Boas-vindas {nome}")

#NOTE - ATIVIDADE 4

#titulo
print(30*"-","ATIVIDADE 4",30*"-")

#dados
n1 = "20"
n2 = 20

#mostrando o tipo de dado da variavel n1
print(f"O tipo de variavel n1 é {type(n1)}")

#transformando o tipo de dado de string para inteiro
n1 = int(n1)
print(f"O tipo de variavel n1 é {type(n1)}")

#somando os dois
soma = n1+n2
print(f"A soma: {n1} + {n2} = {soma}")