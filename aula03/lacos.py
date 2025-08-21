'''
#NOTE - problema: crie um sistema que calcule o indice de massa corporal (IMS)
do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
no peso ideal ou se precisa emagracer ou engordar mais. Utilize a tabela 
do IMC para definir o valor.
'''
'''
#NOTE - WHILE TRUE vai rodar o codigo ate o codigo dar break
'''
'''
while True:
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
    #perguntando se o usuario quer continuar
    opcao = str(input(f"Deseja calcular novamente? \nS - sim | N - não ").lower())
    #if e else para saber se ele quer calcular de  novo
    if opcao == "s":
        break
    elif opcao == "n":
        print(f"Saindo do sistema.")
        break
    else:
        print(f"Opção invalida.")
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
'''
#NOTE - WHILE é um codigo usado para uma condição
significa enquanto algo estiver verdadeiro o codigo vai rodar
'''
'''
#titulo
print(30*"-","Loop de repetição",30*"-")
#variavel
contagem = 10
#loop de 1 a 10
while contagem >= 0:
    print(f"{contagem}")
    contagem -= 1
'''
'''
#NOTE - BREAK é um codigo que acaba com o codigo
mata ele direto
'''
'''
#titulo
print(30*"-","break",30*"-")
#variavel
cont = 0
#contagem de par e impar
while cont < 10:
    cont += 1
    if cont % 2 == 0:
        print(f"{cont}")
    else:
        break
    print(f"Contando...")
'''
'''
#NOTE - PASS é um codigo que ignora os codigos dentro da caixa de codigo
'''
'''
#titulo
print(30*"-","Break",30*"-")
#variavel
cont1 = 0
#loop de contagem
while cont1 < 15:
    cont1 += 1
    if cont1 % 2 == 0:
        print(f"{cont1}")
    elif cont1 >=5:
        pass
    elif cont1 >=7:
        break
    else:
        break
    print(f"Contando...")
'''
'''
#titulo
print(30*"-","Entrada de nome",30*"-")
#variavel
nome1 = str(input(f"Digite o seu nome ou deixe em branco para fechar o programa. "))
#loop
while True:
    #if e else para controlar se o nome foi digitado ou nao
    if nome1 != "":
        print(f"Boas vindas {nome1}.")
        break
    else:
        print(f"Fechando programa.")
        break
'''
#titulo
print(30*"-","Bem-vindo",30*"-")
#coleta de dados
nome = str(input(f"Digite seu nome?: ").upper())
cpf = float(input(f"Digite seu CPF: "))
telefone = int(input(f"Digite seu telefone: "))
dt = int(input(f"Digite seu ano de nascimento: "))
#loop
while True:
    #titulo
    print(30*"-","Sistema de controle 2DS",30*"-")
    print()
    #opção
    print(f"1 - Calculadora IMC.")
    print(f"2 - Maioridade.")
    print(f"3 - Calculadora.")
    print(f"4 - Dados pessoais.")
    print(f"5 - Feliz natal.")
    print(f"6 - Sair.")
    print()
    #pedir uma opcao
    escolha = int(input(f"Escolha um programa: "))

    #calculadora IMC
    if escolha == 1:
        #loop
        while True:
            #titulo
            print(30*"-","Calculadora de IMC",30*"-")
            #pedir informação de peso e altura
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
            #perguntando se o usuario quer continuar
            opcao = str(input(f"Deseja calcular novamente? \nS - sim | N - não ").lower())
            #if e else para saber se ele quer calcular de  novo
            if opcao == "s":
                continue
            elif opcao == "n":
                print(f"Saindo do sistema.")
                break
            else:
                print(f"Opção invalida.")

    #maioridade
    elif escolha == 2:
        #titulo
        print(30*"-","Verificação de maioridade",30*"-")
        #variavel
        ano = 2025
        idade = ano - dt
        if idade >= 18:
            print(f"{nome} é maior de idade.")
            continue
        else:
            print(f"{nome} é menor de idade.")
            continue

    #calculadora
    elif escolha == 3:
        #loop
        while True:
            #titulo
            print(30*"-","Calculadora",30*"-")
            print()
            print("1 - Soma.")
            print("2 - Divisão.")
            print("3 - Subtração.")
            print("4 - Multiplicação.")
            print("5 - Sair")
            print()
            #perguntar a escolha
            opcao_calculo = int(input(f"Escolha uma operação matematica: "))
            #escolha
            #soma
            if opcao_calculo == 1:
                n1 = float(input(f"DIgite o seu primeiro numero: "))
                n2 = float(input(f"DIgite o seu segundo numero: "))
                print(f"A soma dos seu valores: {n1} + {n2} = {n1+n2}")
            #divisao
            elif opcao_calculo == 2:
                n1 = float(input(f"DIgite o seu primeiro numero: "))
                n2 = float(input(f"DIgite o seu segundo numero: "))
                print(f"A divisão dos seu valores: {n1} / {n2} = {n1/n2}")
            #subtração
            elif opcao_calculo == 3:
                n1 = float(input(f"DIgite o seu primeiro numero: "))
                n2 = float(input(f"DIgite o seu segundo numero: "))
                print(f"A subtração dos seu valores: {n1} - {n2} = {n1-n2}")
            #multiplicação
            elif opcao_calculo == 4:
                n1 = float(input(f"DIgite o seu primeiro numero: "))
                n2 = float(input(f"DIgite o seu segundo numero: "))
                print(f"A multiplicação dos seu valores: {n1} * {n2} = {n1*n2}")
            #sair
            elif opcao_calculo == 5:
                break
            #se escolher um valor invalido
            else:
                print(f"Escolha invalida.")

    #dados pessoais
    elif escolha == 4:
        #titulo
        print(30*"-","Coleta de dados pessoais",30*"-")
        #mostra informações
        print(f"| Nome: {nome} |\n| Telefone: {telefone} |\n| CPF: {cpf} |\n| Data de nascimento: {dt} |")
        continue

    #arvore de natal
    elif escolha == 5:
        #titulo
        print(30*"-","Arvore de natal",30*"-")
        #variaveis
        linhas = 15
        j = 1
        #loop
        while j<=linhas:
            #variaveis
            espacos = linhas - j
            estrelas = 2*j-1
            #fazendo arvore
            print(" "*espacos+ "^"*estrelas)
            j+=1
        continue

    #escolha pra sair
    elif escolha == 6:
        break

    #se inserir um numero invalido
    else:
        print(f"opção  invalida.")
        continue
'''
#NOTE - FOR é um codigo para repetir um codigo de forma finita
# que nem o while, mais de forma finita que o codigo define, nao o usuario
'''
'''
#titulo
print(30*"-","FOR",30*"-")
#loop com um tempo limite
for n in range(5):
    print(n+1)
#variavel
nome = "Gomes"
#loop
for i in nome:
    print(i)
'''