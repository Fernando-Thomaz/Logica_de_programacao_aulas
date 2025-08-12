#variaveis
n1 = 10
n2 = 10

#"titulo" na tela
print(40*"-","Operadores",40*"-")

#operadores
soma = n1+n2
divi = n1/n2
mult = n1*n2
expo = n1 ** n2
subt = n1-n2
divi_int = n1//n2
resto = n1 %2

#mostrar as operações na tela
print("Resultado da soma:",n1,"+",n2,"=",soma) #soma
print("Resultado da divisão:",n1,"/",n2,"=",divi) #divisão
print("Resultado da multiplicação:",n1,"*",n2,"=",mult) #multiplicação
print("Resultado do expoente:",n1,"**",n2,"=",expo) #exponencial
print("Resultado da subtração:",n1,"-",n2,"=",subt) #subtração
print("Resultado da divisão inteira:",n1,"//",n2,"=",divi_int) #divisão inteira
print("Resultado do resto de :",n1,"=",resto) #resto da divisão por dois

#"titulo"
print(40*"-","Operadores de atribuição",40*"-")

#operadores de coparação
n1 > n2 #maior que
n1 < n2 #menor que
n1 == n2 #iguais
n1 >= n2 #maior ou igual
n1 <= n2 #menor ou igual
n1 != n2 #diferente que

#operadores de atribuição
ano = 2025 #variavel
acre = 1 #variavel de acrescimo de ano
decre = 1 #variavel de decrescimo do ano

#colocando o ano atual na tela
print("Ano atual:",ano)
ano += acre #atribuição

#mostra o ano adicionando um
print("Depois de",acre,"anos, estaremos em:",ano)
ano -= acre #atribuição
ano -= decre #atribuição

#mostra o ano diminuindo um
print("Se voltamos no tempo a",decre,"anos, estaremos em:",ano)
ano -= decre #atribuição