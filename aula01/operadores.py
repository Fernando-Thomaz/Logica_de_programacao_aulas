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

print(40*"-","Operadores de atribuição",40*"-")

#operadores de coparação
n1 > n2
n1 < n2
n1 == n2
n1 >= n2
n1 <= n2
n1 != n2

#operadores de atribuição
ano = 2025 #variavel
acre = 1 #variavel de acrescimo de ano
decre = 1 #variavel de decrescimo do ano
print("Ano atual:",ano)
ano += acre #atribuição
print("Depois de",acre,"anos, estaremos em:",ano)
ano -= acre #atribuição
ano -= decre #atribuição
print("Se voltamos no tempo a",decre,"anos, estaremos em:",ano)
ano -= decre #atribuição