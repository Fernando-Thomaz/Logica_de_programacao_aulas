'''
problema: crie um sistema que calcule o indice de massa corporal (IMS)
do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
no peso ideal ou se precisa emagracer ou engordar mais. Utilize a tabela 
do IMC para definir o valor.
'''
#variavel
nome = str(input(f"Qual é seu nome? ").upper())
peso = float(input(f"Qual é o seu peso? "))
altura = float(input(f"Qual é a sua altura? ").replace(",","."))

imc = peso/(altura*altura)


print(f"{nome} seu IMC é: {imc:.2f}")

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