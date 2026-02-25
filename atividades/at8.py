# titulo
print(30*'-','TROCA DE NOME','-'*30)

# usuario digita dois nomes e dois sobrenomes
nome1 = input('Digite o primeiro nome: ').strip().title()
sobre1 = input('Digite o primeiro sobrenome: ').strip().title()
nome2 = input('Digite o segundo nome: ').strip().title()
sobre2 = input('Digite o segundo sobrenome: ').strip().title()

# troca os sobrenomes
print(f'O novo nome do primeiro é {nome1} {sobre2}')
print(f'O novo nome do segundo é {nome2} {sobre1}')