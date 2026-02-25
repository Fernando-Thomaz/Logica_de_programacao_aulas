# titulo
print(30*'-','MEDIA ARITMETICA','-'*30)

# usuario digita tres notas
n1 = float(input('Digite a primeira nota: ').replace(',','.'))
n2 = float(input('Digite a segunda nota: ').replace(',','.'))
n3 = float(input('Digite a terceira nota: ').replace(',','.'))

# calcula a media
media = (n1+n2+n3)/3

# mostra o resultado com duas casas decimais
print(f'A média aritmética entre {n1}, {n2} e {n3} é igual a {media:.2f}') 