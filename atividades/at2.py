# tiutlo
print(30*'-','CONVERTER TEMPERATURA','-'*30)

# usuario digita o valor em fanreheit
valor = float(input('Digite a temperatura em fanreheit: ').replace(',','.'))

# converte para celsius
celsius = (valor - 32) * 5/9

# mostra o resultado com duas casas decimais
print(f'A temperatura de {valor}°F corresponde a {celsius:.2f}°C')