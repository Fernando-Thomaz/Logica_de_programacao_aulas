# bibliotecas
import json
import os

# lista de pessoas
usuarios = []
novo_arquivo = ''

# função para usar a variavel limpar para ativar o comando clear
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# loop
while True:
    # dicionario de usuario
    usuario = {}

    # menu
    print(30*'-','MENU DE CADASTRO',30*'-')
    print('1 - Cadastrar novo usuario')
    print('2 - Salvar usuario no arquivo JSON')
    print('3 - Fazer leitura de arquivo JSON')
    print('4 - Sair do sistema')
    print()

    # usuario escolhe
    opcao = input('Escolha a opção desejada: ')

    # limpa codigo
    limpar()

    # tenta rodar o codigo
    try:
        # opcao de escolha
        match opcao:
            case '1':
                # usuario digita suas informações
                usuario['nome'] = str(input('Informe o nome: ')).strip().title()
                usuario['idade'] = int(input('Informe a idade: '))
                usuario['email'] = str(input('Informe o email: ')).strip().lower()

                # adiciona o usuario a lista de usuarios
                usuarios.append(usuario)
            
                # limpa a tela
                limpar()
                print('Usuario cadastrado com sucesso!')
                continue

            case '2':
                # usuario digita o nome do arquivo que ele quer abrir
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()

                # encontra o caminho da pasta que vai ser criada
                with open(fr'C:\GIT\Logica_de_programacao_aulas\aula06/{novo_arquivo}.json','w',encoding='utf-8') as f:
                    # grava o arquivo json
                    json.dump(usuarios,f,ensure_ascii=False,indent=4)

                # limpa tela
                limpar()
                print('Arquivo salvo com sucesso!')
                continue

            case '3':
                # se nao tiver um arquivo
                if not novo_arquivo:
                    # usuario digita o nome do arquivo que quer ler
                    novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()

                # encontra o arquivo que o usuario pediu
                with open(fr'C:\GIT\Logica_de_programacao_aulas\aula06/{novo_arquivo}.json','r',encoding='utf-8') as f:
                    # variavel que tem a leitura do arquivo
                    dados = json.load(f)

                    # titulo
                    print(f'{30*'-'} USUARIOS CADASTRADOS {30*'-'}')

                    # se tive algum dado em dados
                    for usuario in dados:
                        # se tiver alguma chave em dado
                        for chave in usuario:
                            # mostra a chave e o valor
                            print(f'{chave.capitalize()} : {usuario.get(chave)}')
                        print(f'{30*"-"} FIM {30*"-"}')
                    continue

            case '4':
                print('Saindo...')
                break

            case _:
                print('Digite uma opção valida')
                continue

    # caso o codigo quebre
    except Exception as e:
        print(f'ERROR {e}')