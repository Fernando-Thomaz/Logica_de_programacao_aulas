#filme do cinema
sala1 = "Premoniação 6"
sala2 = "Quarteto fantastico"
sala3 = "Coringa"
sala4 = "Como eu era antes de você"
sala5 = "Creed"
id1 = "18"
id2 = "L"
id3 = "16"
id4 = "L"
id5 = "14"
#pedi nome e idade
usuario = str(input(f"DIgite seu nome: "))
ano = int(input(f"Digite sua idade: "))
#loop
while True:
    #titulo
    print(30*"-","Cinemax",30*"-")
    #mostrar os filmes
    print(f"1 - | {sala1} | classificação: {id1} | sala: 6 |")
    print(f"2 - | {sala2} | classificação: {id2} | sala: 3 |")
    print(f"3 - | {sala3} | classificação: {id3} | sala: 1 |")
    print(f"4 - | {sala4} | classificação: {id4} | sala: 4 |")
    print(f"5 - | {sala5} | classificação: {id5} | sala: 2 |")
    print(f"6 - | Sair")
    print()
    #escolher o filme
    filme = str(input(f"Escolha o filme: "))
    print()
    #verificar a classificação indicativa
    if filme == "1":
        if ano>=18:
            print("| ticket")
            print(f"| Filme: {sala1}")
            print("| sala 6")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            print()
            continue
    elif filme == "2":
        print("| ticket")
        print(f"| Filme: {sala2}")
        print("| sala 3")
        break
    elif filme == "3":
        if ano>=16:
            print("| ticket")
            print(f"| Filme: {sala3}")
            print("| sala 1")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            print()
            continue
    elif filme == "4":
        print("| ticket")
        print(f"| Filme: {sala4}")
        print("| sala 4")
        break
    elif filme == "5":
        if ano>=14:
            print("| ticket")
            print(f"| Filme: {sala5}")
            print("| sala 2")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            print()
            continue
    elif filme == "6":
        print("Saindo...")
        break
    #se a informação for invalida
    else:
        print("Invalido")
        print()
        continue