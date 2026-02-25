# titulo
print(30*'-','CONVERTER DINHEIRO','-'*30)

# usuario digita o valor em dolar
dolar = float(input('Digite o valor em dolar: ').replace(',','.'))

# calcula o valor em reais
reais = dolar * 5.41

# mostra o resultado com duas casas decimaisw
print(f'O valor de R${reais:.2f} corresponde a US${dolar:.2f}')