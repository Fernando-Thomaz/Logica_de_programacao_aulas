# Classe - espaço onde vou descrever um objeto
    # Atributos - caracteristicas do objeto
    # Metodos - ações desse objeto

# Nome e vida - atacar
# Self - quando quero me referir a algum atributo da classe
# Construtor - quando quero criar um novo objeto chamo o construtor para acessar os atributos

# Biblioteca
import os

# Classe pai
class Personagem:
    # Construtor
    def __init__(self, nome, vida, defender=False, morto=False):
        # Definir e encapsulando o nome e a vida do personagem
        self.__nome = nome
        self.__morto = morto
        self.__defender = defender
        self.__vida = vida

    # Definindo GET e SET
    # GET
    @property
    def nome(self):
        return self.__nome
    
    # SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # GET
    @property
    def morto(self):
        return self.__morto
    
    # SET
    @morto.setter
    def morto(self, morte):
        self.__morto = morte

    # GET
    @property
    def defender(self):
        return self.__defender
    
    # SET
    @defender.setter
    def defender(self, defender):
        self.__defender = defender

    # GET
    @property
    def vida(self):
        return self.__vida
    
    # SET
    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

    # Função de defender
    def defende(self):
        self.defender = True
        print(f"{self.nome} está defendendo.")

    # Função de atacar
    def atacar(self, personagem):
        # Dano
        ataque = 20
        # Se o personagem estiver defendendo
        if personagem.defender == True:
            # Ataque reduzido pela metade
            ataque = ataque/2
            personagem.vida -= ataque
            
            # Desativa a defesa
            personagem.defender = False

            print(f"{self.nome} atacou {personagem.nome} e ele defendeu.")
        # se não
        else:
            # Reduz a vida do oponente
            personagem.vida -= ataque
            print(f"{self.nome} atacou {personagem.nome} e tirou {ataque} pontos de vida.")
        print(f"{personagem.nome} está com {personagem.vida} de vida.")

# Classe guerreiro
class Guerreiro(Personagem):
    # Construtor
    def __init__(self, nome, vida, defender=True):
        super().__init__(nome, vida, defender)

    def defende(self):
        return super().defende()

    # Função de atacar
    def atacar(self, personagem):
        # Dano
        ataque = 25
        # Se o personagem estiver defendendo
        if personagem.defender == True:
            # Ataque reduzido pela metade
            ataque = ataque/2
            personagem.vida -= ataque
            
            # Desativa a defesa
            personagem.defender = False

            print(f"{self.nome} atacou {personagem.nome} e ele defendeu.")
        # se não
        else:
            # Reduz a vida do oponente
            personagem.vida -= ataque
            print(f"{self.nome} atacou {personagem.nome} e tirou {ataque} pontos de vida.")
        print(f"{personagem.nome} está com {personagem.vida} de vida.")

# Classe mago
class Mago(Personagem):
    # Construtor
    def __init__(self, nome, vida, defender=False):
        super().__init__(nome, vida, defender)

    def defende(self):
        return super().defende()

    # Função de ataque
    def atacar(self, personagem):
        # Dano
        ataque = 15
        # Se o personagem estiver defendendo
        if personagem.defender == True:
            # Ataque reduzido pela metade
            ataque = ataque/2
            personagem.vida -= ataque
            
            # Desativa a defesa
            personagem.defender = False

            print(f"{self.nome} atacou {personagem.nome} e ele defendeu.")
        # se não
        else:
            # Reduz a vida do oponente
            personagem.vida -= ataque
            print(f"{self.nome} atacou {personagem.nome} e tirou {ataque} pontos de vida.")
        print(f"{personagem.nome} está com {personagem.vida} de vida.")

    # Função de cura
    def curar(self, personagem):
        if personagem == self:
            self.vida += 15
            print(f"{self.nome} se curou.")
            print(f"{self.nome} está com {self.vida} de vida.")
        else:
            personagem.vida += 20
            print(f"{self.nome} usou o poder de cura em {personagem.nome}.")
            print(f"A vida de {personagem.nome} agora é de {personagem.vida}.")

# Classe vapiro
class Vampiro(Personagem):
    # Construtor
    def __init__(self, nome, vida, defender=False):
        super().__init__(nome, vida, defender)

    def defende(self):
        return super().defende()

    # Função de ataque
    def atacar(self, personagem):
        # Dano
        ataque = 20
        # Vampirismo
        cura = 10
        # Se o personagem estiver defendendo
        if personagem.defender == True:
            # Ataque reduzido pela metade
            ataque = ataque/2
            personagem.vida -= ataque
            
            # se cura
            self.vida += ataque/2

            # Desativa a defesa
            personagem.defender = False

            print(f"{self.nome} atacou {personagem.nome} e ele defendeu.")
        # se não
        else:
            # Reduz a vida do oponente
            personagem.vida -= ataque
            self.vida += ataque/2
            print(f"{self.nome} atacou {personagem.nome} e tirou {ataque} pontos de vida.")
        print(f"{personagem.nome} está com {personagem.vida} de vida.")
        print(f"{self.nome} roubou {cura} de vida do inimigo, {self.nome} está com {self.vida} de vida.")

# personagens
fernando = Vampiro("Fernando", 15)
lucas = Guerreiro("Lucas", 10)
andre = Mago("Andre", 20)

# Loop
while True:
    # Round do fernando
    while True:
        if fernando.vida >= 1:
            print(f"Round do Fernando")
            print(f"1 - atacar")
            print(f"2 - defender")
            
            # Usuario escolhe
            acao = input(f"Digite uma opção: ")

            # possiveis escolhas
            match acao:
                case "1":
                    print(f"1 - lucas")
                    print(f"2 - Andre")
                    
                    # Usuario esolhe
                    pessoa = input(f"Quem você quer atacar? ")
                    if pessoa == "1":
                        fernando.atacar(lucas)
                        break
                    elif pessoa == "2":
                        fernando.atacar(andre)
                        break
                    else:
                        print(f"Digite uma das opções.")
                        continue
                case "2":
                    fernando.defende()
                    break
                case Exception:
                    print(f"Digite uma das opções.")
        
        else:
            print(f"{fernando.nome} morreu")
            break

    # Round do lucas
    while True:
        if lucas.vida >= 1:
            print(f"Round do Lucas")
            print(f"1 - atacar")
            print(f"2 - defender")
            
            # Usuario escolhe
            acao = input(f"Digite uma opção: ")

            # possiveis escolhas
            match acao:
                case "1":
                    print(f"1 - Fernando")
                    print(f"2 - Andre")
                    
                    # Usuario esolhe
                    pessoa = input(f"Quem você quer atacar? ")
                    if pessoa == "1":
                        lucas.atacar(fernando)
                        break
                    elif pessoa == "2":
                        lucas.atacar(andre)
                        break
                    else:
                        print(f"Digite uma das opções.")
                        continue
                case "2":
                    lucas.defende()
                    break
                case Exception:
                    print(f"Digite uma das opções.")
        else:
            print(f"{lucas.nome} morreu")
            break

    # Round do andre
    while True:
        if andre.vida >= 1:
            print(f"Round do Andre")
            print(f"1 - atacar")
            print(f"2 - defender")
            print(f"3 - curar")
            
            # Usuario escolhe
            acao = input(f"Digite uma opção: ")

            # possiveis escolhas
            match acao:
                case "1":
                    print(f"1 - Fernando")
                    print(f"2 - Lucas")
                    
                    # Usuario esolhe
                    pessoa = input(f"Quem você quer atacar? ")
                    if pessoa == "1":
                        andre.atacar(fernando)
                        break
                    elif pessoa == "2":
                        andre.atacar(lucas)
                        break
                    else:
                        print(f"Digite uma das opções.")
                        continue
                case "2":
                    andre.defende()
                    break
                case "3":
                    print(f"1 - Fernando")
                    print(f"2 - Lucas")
                    print(f"3 - Andre")

                    # Usuario esolhe
                    pessoa = input(f"Quem você quer curar? ")
                    if pessoa == "1":
                        andre.curar(fernando)
                        break
                    elif pessoa == "2":
                        andre.curar(lucas)
                        break
                    elif pessoa == "3":
                        andre.curar(andre)
                        break
                    else:
                        print(f"Digite uma das opções.")
                        continue
                case Exception:
                    print(f"Digite uma das opções.")
        else:
            print(f"{andre.nome} morreu")
            break

    # Fim de round
    print(f"Fim dos rounds")
    input(f"Pressione ENTER para continuar")

    # verificação de vitoria
    if fernando.vida <= 0 and lucas.vida <= 0:
        print(f"{andre.nome} ganhou")
        break
    if andre.vida <= 0 and lucas.vida <= 0:
        print(f"{fernando.nome} ganhou")
        break
    if fernando.vida <= 0 and andre.vida <= 0:
        print(f"{lucas.nome} ganhou")
        break

    # limpa tela
    os.system('cls' if os.name == 'nt' else 'clear')