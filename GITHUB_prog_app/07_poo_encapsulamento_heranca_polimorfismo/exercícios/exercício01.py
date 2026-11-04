#Personagens de um jogo de RPG

#Encapsulamento

class Personagem:
    def __init__(self, nome, vida = 100):
        self.nome = nome
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida

    def receber_dano(self, dano):
        if dano < 0:
            print(f"Dano negativo")
        else:
            if (self.__vida - dano) < 0:
                print(f"Dano inválido")
            elif (self.__vida - dano) == 0:
                print(f"Morreu")
                self.__vida = self.__vida - dano
            else:
                print(f"Recebeu dano")
                self.__vida = self.__vida - dano

    def curar(self, cura):
        if cura < 0:
            print(f"Cura negativo")
        else:
            if (self.__vida + cura) > 100:
                print(f"Cura Invalida")
            elif (self.__vida - cura) == 0:
                print(f"Morreu")
                self.__vida = self.__vida + cura
            else:
                print(f"Recebeu cura")
                self.__vida = self.__vida + cura

    def status(self):
        print(f"Nome do personagem: {self.nome}\nVida atual: {self.__vida}")

    def atacar(self):
        return "10"

print("Personagem")
diel = Personagem("Diel")
diel.receber_dano(-70)
diel.receber_dano(110)
diel.receber_dano(10)
diel.curar(50)

try:
    diel.vida = 200
except AttributeError:
    print("O atributo __vida não pode ser acessado de fora.")

diel.status()
diel.atacar()
print(f"Ataque: {diel.atacar()}")

print("\n\n")

#Herança

class Guerreiro(Personagem):
    def __init__(self, nome, forca, vida = 100):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        return 10 + self.forca

class Mago(Personagem):
    def __init__(self, nome, mana, vida = 100):
        super().__init__(nome, vida)
        self.mana = mana

    def mana(self):
       self.mana = 50
       print(f"Mana do Mago é {self.mana}")

    def atacar(self):
        if self.mana >= 10:
            mana = self.mana - 10
            print(f"Ataque: 25")
        else:
            print(f"Mana insuficiente, ataque: 5")

borges = Guerreiro("Borges", 80)
fran = Mago("Fran", 67)

print("Guerreiro")
borges.receber_dano(20)
borges.curar(10)
borges.atacar()
print(f"Ataque: {borges.atacar()}")
borges.status()

print("\n\n")

print("Mago")
fran.receber_dano(90)
fran.curar(80)
fran.atacar()
fran.status()
print(f"Isinstance verdadeira? {isinstance(fran, Personagem)}")