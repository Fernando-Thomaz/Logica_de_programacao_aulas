#"titulo na tela"
print(40*"-","Entrada de dados",40*"-")

#codigo que pede a entrada de dados "nome"
nome_usuario = input("Digite o seu nome: ")
print("Seja bem-vindo ao seu sistema python",nome_usuario)

#"titulo"
print(40*"-","Calculadora",40*"-")

#pedindo a entrada de dados da calculadora
n1 = float(input("Digite o primiero número:"))
n2 = float(input("Digite o segundo número:"))
'''
Tipos de dados:
float = números reais, ou seja, números com virgula, EX: 5.20
int = números inteiro
str = texto, conjunto de caracteres
bool = valores logicos, true ou false, 1 ou 0
'''

#calculo
soma = n1+n2
sub = n1-n2
divi = n1/n2
divi_int = n1//n2
mult = n1*n2
expo = n1**n2
resto = n1 %2

#mostrar os calculos da calculadora
print("Resultado da soma:",n1,"+",n2,"=",soma) #soma
print("Resultado da divisão:",n1,"/",n2,"=",divi) #divisão
print("Resultado da multiplicação:",n1,"*",n2,"=",mult) #multiplicação
print("Resultado do expoente:",n1,"**",n2,"=",expo) #exponencial
print("Resultado da subtração:",n1,"-",n2,"=",sub) #subtração
print("Resultado da divisão inteira:",n1,"//",n2,"=",divi_int) #divisão inteira
print("Resultado do resto de :",n1,"=",resto) #resto da divisão por dois