#biblioteca
import os

# loop
while True:
    
    # tenta rodar o codigo
    try:
        # limpa a tela
        os.system("cls")

        # titulo
        print(30*"-","Calculo de combustivel",30*"-")

        # usuario digita o preco do etanol e da gasolina
        etanol = float(input(f"Digite o preço do etanol: ").replace(",","."))
        gasolina = float(input(f"Digite o preço da gasolina: ").replace(",","."))

        # calculo para ver qual vale mais a pena
        calculo = (etanol/gasolina)*100

        # mostra o resultado
        resultado = "Gasolina" if calculo > 70 else "Etanol"
        print(f"Resultado = {calculo:.2f}%. Compensa abastecer com {resultado}.")

        # usuario escolhe se quer refazer o calculo
        escolha = str(input("Deseja refazer o calculo( S - sim | N - não )? ").lower().strip())

        # possiveis escolhas do usuario
        match escolha:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção invalida!")
                continue
    
    # mostra o erro
    # EXCEPTION serve para mostrar o erro causado
    except Exception as e:
        print(f"Digite um numero!\nErro:{e}")
        input("Pressione ENTER para continuar")