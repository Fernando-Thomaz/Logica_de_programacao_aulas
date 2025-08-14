'''
#NOTE - problema: crie um sistema que calcule o indice de massa corporal (IMS)
do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
no peso ideal ou se precisa emagracer ou engordar mais. Utilize a tabela 
do IMC para definir o valor.
'''
'''
#titulo
print(30*"-","Calculadora de IMC",30*"-")

#variavel
nome = str(input(f"Qual é seu nome? ").upper())
peso = float(input(f"Qual é o seu peso? ").replace(",","."))
altura = float(input(f"Qual é a sua altura? ").replace(",","."))

#calculo do IMC
imc = peso/(altura*altura)

#mostrando o IMC da pessoa
print(f"{nome} seu IMC é: {imc:.2f}")

#if e else do IMC
if imc <= 18.4:
    print(f"Você esta abaixo do peso normal.")
elif imc <= 24.9:
    print(f"Você esta com o peso ideal.")
elif imc <= 29.9:
    print(f"Você esta sobrepeso.")
elif imc <= 34.9:
    print(f"Você esta com obesidade grau I.")
elif imc <= 39.9:
    print(f"Você esta com obesidade grau II.")
else:
    print(f"Você esta com obesidade grau III.")
    
'''
'''
#NOTE - Problema 2: Um elevador de carga possui capacidade maxima de 200kg. Crie
um programa que receba do usuario seu peso e o peso da carga e verifica
se a carga esta autorizada a usar o elevador ou nao.
'''
'''
#titulo
print(30*"-","Elevador",30*"-")

#variavel
limite = 200
peso2 = float(input(f"Qual é o seu peso? ").replace(",","."))
carga = float(input(f"Qual é a carga que você esta levando? ").replace(",","."))

#calculo da soma total, da carga com o peso da pessoa
soma = carga+peso2

#mostrar o limite de peso e a carga total da pessoa
print(f"O limite de carga é: {limite}")
print(f"Seu peso: {soma}")

#if e else do limite de carga autorizada no elevador
if soma >= limite:
    print(f"Infelizmente não podemos deixar você entrar no elevador, porque você excede o peso maximo.")
else:
    print(f"Você pode usar o elevador.")
'''