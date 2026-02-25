#NOTE - Função
def calcular_equaçao_primeior_grau(a, b):
    x = -b / a
    # devolve o valor de x
    return x

def exibir_mensagem(nome):
    print(f'{30*'-'}Bem vindo ao sistema{30*'-'}')
    print(f'Ola {nome} você esta na aula 07 de Python')

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# usuario insere o nome
nome = input('Digite seu nome: ').title().strip()

# usuario deve responder com S ou N
decisao = str(input('Deseja exibir a mensagem? [S/N]: ')).upper().strip()

# posiveis respostas
match decisao:
    case 'S':
        # chama a função com o nome como argumento
        exibir_mensagem(nome)
    
    case 'N':
        print('Ok, você não verá a mensagem.')
    
    case _:
        print('Opção inválida. Por favor, responda com S ou N.')

decisao2 = str(input('Deseja resolver uma equação do 1º grau? [S/N]: ')).upper().strip()

match decisao2:
    case 'S':
        # usuario insere os valores de a e b
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        
        # chama a função para calcular a equação
        resultado = calcular_equaçao_primeior_grau(a, b)
        
        # exibe o resultado
        print(f'O valor de x na equação {a}x + {b} = 0 é: {resultado}')
    
    case 'N':
        print('Ok, você não resolverá a equação.')
    
    case _:
        print('Opção inválida. Por favor, responda com S ou N.')

decisao3 = str(input('Deseja calcular o fatorial de um número? [S/N]: ')).upper().strip()

match decisao3:
    case 'S':
        # usuario insere o valor de n
        n = int(input('Digite um número inteiro não negativo: '))
        
        # chama a função para calcular o fatorial
        fatorial = calcular_fatorial(n)
        
        # exibe o resultado
        print(f'O fatorial de {n} é: {fatorial}')

    case 'N':
        print('Ok, você não calculará o fatorial.')

    case _:
        print('Opção inválida. Por favor, responda com S ou N.')

