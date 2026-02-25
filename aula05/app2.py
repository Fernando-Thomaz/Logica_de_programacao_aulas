'''
Programa: manipulaçao de arquivos 1.0
'''

# biblioteca
import os

# loop
while True:
    try:
        # usuario digita o nome do arquivo
        arquivo = input("Digite o nome do arquivo (sem extensão) ou pressione ENTER para fechar o programa: ").lower().strip()

        if arquivo == "":
            print("saindo...")
            break

        else:
            # chama o arquivo
            with open(f"{arquivo}.txt","r",encoding="utf-8") as f:
                arquivo_abrir = f.read()
            
            # limpa a tela
            os.system("cls" if os.name == "nt" else "clear")

            # mostrar os dados do arquivo
            print(arquivo_abrir)

            # loop
            while True:
                # usuario digita se quer abrir outro arquivo
                prosseguir = input("Deseja abrir outros arquivos?\n(s/n): ")

                # se for sim ou nao ele via continuar o codigo
                if prosseguir == "s" or prosseguir == "n":
                    break

                # se for outra coisa o codigo repete ate ter uma resposta valida
                else:
                    print("Opção invalida!")
                    continue
            
            # possiveis respostas
            match prosseguir:
                # se for sim
                case "s":
                    continue

                # se for nao
                case "n":
                    break

        # se o codigo dar error
    except Exception as e:
        print(f"ERROR\nO erro foi:{e}")
        input("Pressione ENTER para continuar")