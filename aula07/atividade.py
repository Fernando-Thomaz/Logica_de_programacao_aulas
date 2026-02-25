# biblioteca
import os
import json
from funcoes import criar_conta, exibir_dados, depositar_valor, sacar_valor, menu, encerrar_conta

# loop principal
while True:
    # tratando erros
    try:
        # possiveis escolhas
        match menu():
            # caso queira criar conta
            case 1:
                criar_conta()

            # caso queira exibir dados da conta
            case 2:
                exibir_dados()

            # caso queira depositar valor
            case 3:
                depositar_valor()

            # caso queira sacar valor
            case 4:
                sacar_valor()

            case 5:
                encerrar_conta()

            # caso queira sair
            case 6:
                print('Saindo do sistema...')
                break

            # caso a escolha seja inválida
            case _:
                print('Opção inválida. Por favor, escolha uma opção entre 1 e 6.')
                continue

    # tratando erros gerais
    except Exception as e:
        print(f'Erro: {e}. Por favor, tente novamente.')
        input('Pressione ENTER para continuar...')
        continue