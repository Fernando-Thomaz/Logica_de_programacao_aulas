#NOTE - contagem regressiva | importando biblioteca
import os
#se quiser importar apenas os comandos usados daquela biblioteca
from time import sleep
#pedir o numero para a contagem regressiva
cont = int(input(f"DIgite um número inteiro: "))
try:
    while cont >= 0:
        os.system("cls")
        print(f"Contagem regressiva: {cont}...")
        sleep(1)
        cont -= 1
        os.system("cls")
except:
    print(f"Digite um número valido")
print(f"Fim da contagem!")