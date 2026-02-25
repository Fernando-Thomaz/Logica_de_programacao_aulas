# titulo
print(30*'-','VERIFICAÇÃO DE NUMERO MAIOR','-'*30)

# usuario digita dois numeros
n1 = float(input('Digite o primeiro numero: ').replace(',','.'))
n2 = float(input('Digite o segundo numero: ').replace(',','.'))

# se n1 for maior que n2
if n1 > n2:
    print(f'O numero {n1} é maior que {n2}')

# se n2 for maior que n1
elif n2 > n1:
    print(f'O numero {n2} é maior que {n1}')

# se os dois forem iguais
else:
    print('Os numeros são iguais')