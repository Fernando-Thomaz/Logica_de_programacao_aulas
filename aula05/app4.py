'''
Programa: manipulação de arquivos 3.0
'''
# biblioteca
import os

# loop
while True:
    # tenta rodar o codigo
    try:
        # titulo
        print(30*"-","Manipulação de arquivo",30*"-")

        # usuario digita o texto e cira um arquivo
        novo_texto = input("Digite o texto: ")
        novo_arquivo = input("Digite o nome do arquivo (sem extensão) ou pressione ENTER para cancelar: ").strip().lower()

        # se o usuario digitar algo
        if novo_arquivo != "":

            # abre o arquivo para sobre escrever o texto
            with open(fr"C:\GIT\Logica_de_programacao_aulas\aula05/{novo_arquivo}.txt","w", encoding="utf-8") as f:
                # escreve o texto no arquivo
                f.write(novo_texto)

            # limpa a tela
            os.system("cls" if os.name == "nt" else "clear")

            # avisa que foi gravado
            print(f"{novo_arquivo}.txt foi gravado com sucesso!!")

            # usuario digita um novo texto
            novo_texto_add = input("Digite o novo texto: ")

            # abre o arquivo para adicionar um texto
            with open(fr"C:\GIT\Logica_de_programacao_aulas\aula05/{novo_arquivo}.txt","a",encoding="utf-8") as f:
                f.write(novo_texto_add)
            print("Gravado com sucesso!!")

            #atualiza a pasta
            with open(f"{novo_arquivo}.txt","r",encoding="utf-8") as f:
                texto_final = f.read()
            print(f"Texto final: {texto_final}")

            # loop 2
            while True:
                # usuario digita se quer abrir outro arquivo
                prosseguir = input("Deseja abrir outro arquivo? (s/n): ").lower()
                
                # se prosseguir for sim ou nao
                if prosseguir == "s" or "n":
                    break

                # se for outra coisa
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
                    print("Saindo...")
                    break

        # se o usuario escolher sair
        else:
            print("Saindo...")
            break

    # se o codigo quebrar
    except Exception as e:
        print(f"ERROR!!\nErro: {e}")