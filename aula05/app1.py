# NOTE - manipulação de arquivos
# leitura de arquivos
# WITH abre um arquivo que esta no repertorio
# (pasta que ele vai abrir,se ele vai ler ou escrever ("r" ou "W"),como ele vai ler (a normal e a UTF-8))
with open("text.txt","r",encoding="utf-8") as f:
    texto = f.read()

print(texto)