import os
import json

# funções
def criar_conta():
    # variaveis globais
    global nome, idade, saldo, senha

    # usuario insere os dados
    nome = str(input('Digite seu nome: ')).title().strip()
    idade = int(input('Digite sua idade: '))
    senha = str(input('Crie uma senha: ')).strip()
    saldo = 0.0

    # salvando os dados em um arquivo json
    with open('conta.json', 'w') as f:
        json.dump({'nome': nome, 'idade': idade, 'senha': senha, 'saldo': saldo}, f)
    print('Conta criada com sucesso!')
    input('Pressione ENTER para continuar...')

def exibir_dados():
    # verifica se tem uma conta criada
    if nome == '':
        print('Nenhuma conta cadastrada. Por favor, crie uma conta primeiro.')
        input('Pressione ENTER para continuar...')

    else:
        # lendo os dados do arquivo json
        with open('conta.json', 'r') as f:
            conta = json.load(f)

        # exibindo os dados
        print(f'Nome: {conta["nome"]}')
        print(f'Idade: {conta["idade"]}')
        print(f'Saldo: R${conta["saldo"]:.2f}')
        input('Pressione ENTER para continuar...')

def depositar_valor():
    # variaveis globais
    global saldo, valor

    # usuario insere a senha para continuar
    senha_input = str(input('Digite sua senha para continuar: ')).strip()
    if senha_input != senha:
        print('Senha incorreta. Operação cancelada.')
        input('Pressione ENTER para continuar...')
        return
    
    else:
        # usuario insere o valor a ser depositado
        valor = float(input('Digite o valor a ser depositado: '))

        # verificando se o valor é positivo
        if valor > 0:
            saldo += valor

            # salvando o novo saldo no arquivo json
            with open('conta.json', 'w') as f:
                json.dump({'nome': nome, 'idade': idade, 'senha': senha, 'saldo': saldo}, f)
            print(f'Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}')
            input('Pressione ENTER para continuar...')

        else:
            print('Valor de depósito inválido. Por favor, insira um valor positivo.')
            input('Pressione ENTER para continuar...')

def sacar_valor():
    # variaveis globais
    global saldo, valor_sacar

    # usuario insere a senha para continuar
    senha_input = str(input('Digite sua senha para continuar: ')).strip()

    # verificando se a senha está correta
    if senha_input != senha:
        print('Senha incorreta. Operação cancelada.')
        input('Pressione ENTER para continuar...')

    else:
        # usuario insere o valor a ser sacado
        valor_sacar = float(input('Digite o valor a ser sacado: '))

        # verificando se o valor é positivo e se tem saldo suficiente
        if valor_sacar > 0:
            if valor_sacar <= saldo:
                saldo -= valor_sacar

                # salvando o novo saldo no arquivo json
                with open('conta.json', 'w') as f:
                    json.dump({'nome': nome, 'idade': idade, 'senha': senha, 'saldo': saldo}, f)
                print(f'Saque de R${valor_sacar:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}')
                input('Pressione ENTER para continuar...')

            else:
                print('Saldo insuficiente para realizar o saque.')
                input('Pressione ENTER para continuar...')

        else:
            print('Valor de saque inválido. Por favor, insira um valor positivo.')
            input('Pressione ENTER para continuar...')

def encerrar_conta():
    # usuario insere a senha para continuar
    senha_input = str(input('Digite sua senha para continuar: ')).strip()
    if senha_input != senha:
        print('Senha incorreta. Operação cancelada.')
        input('Pressione ENTER para continuar...')
        
    else:
        # verificando se o saldo é zero
        if saldo != 0:
            print('Para encerrar a conta, o saldo deve ser zero. Por favor, saque ou deposite o valor necessário.')
            input('Pressione ENTER para continuar...')
            return
        
        else:
            # apagando os dados do arquivo json
            with open('conta.json', 'w') as f:
                f.write('')
        print('Conta encerrada com sucesso.')
        input('Pressione ENTER para continuar...')

def menu():
    # limpando a tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # titulo
        print(f'{"-"*30}BANCO{"-"*30}')

        # menu
        print('1 - Criar conta')
        print('2 - Exibir dados da conta')
        print('3 - Depositar valor')
        print('4 - Sacar valor')
        print('5 - Encerrar conta')
        print('6 - Sair do sistema')
        print()

        # usuario escolhe uma opção
        escolha = int(input('Escolha uma opção (1-6): '))
        return escolha