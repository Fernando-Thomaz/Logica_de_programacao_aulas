# biblioteca
import json

# tenta rodar o codigo
try:
    # usuario digita o nome do arquivo
    arquivo = input("Digite o nome do arquivo: ").strip().lower()

    # encontra o arquivo que o usuario pediu
    with open(f"{arquivo}.json","r",encoding="utf-8") as f:
        # variavel que tem a leitura do arquivo
        dados = json.load(f)

    # titulo
    print(f"{30*"-"} DADOS {30*"-"}")

    # se tive algum dado em dados
    for dado in dados:
        # se tiver alguma chave em dado
        for chave in dado:
            print(f"{chave.capitalize()} : {dado.get(chave)}")
        
        # titulo fim
        print(f"{30*"-"} FIM {30*"-"}")

# se o codigo quebrar
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")