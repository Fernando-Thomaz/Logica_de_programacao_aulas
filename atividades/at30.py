'''
ERRADO
x = input(int('Digite um numero: '))

for num in range(1,11):
    print({x} X {num} = x*num)
ERRADO
'''
# titulo
print(30*'-','TABUADA','-'*30)

# usuario digita um numero
x = int(input('Digite um numero para ver a tabuada: '))
# mostra a tabuada do numero digitado
for num in range(1,11):
    print(f'{x} x {num} = {x*num}')