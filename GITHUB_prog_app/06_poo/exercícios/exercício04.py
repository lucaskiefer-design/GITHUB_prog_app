#Personagem de Videogame

class PersonagemVideogame:
    def __init__(self, nome, classe, vida = 100, nivel = 1):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.nivel = nivel

    def receber_dano(self, dano):
        self.vida = self.vida - dano
        if self.vida <= 0:
            print (f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} tá vivo")

    def curar(self, cura):
        self.vida08 = self.vida + cura
        if self.vida1 > 100:
            print (f"Cura deu errado!")
        else:
            print(f"Curado")
        self.vida == self.vida08

    def subir_nivel(self):
        self.nivel = self.nivel + 1
        self.vida = 100
        print(f"Nível subido! Nível: {self.nivel}, Vida: {self.vida}")

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.nivel}, Vida: {self.vida}")

        if self.vida <= 0:
            print(f"{self.nome} morreu!")


personagem1 = PersonagemVideogame("Gandalf", "Mago")
personagem2 = PersonagemVideogame("Boromir", "Guerreiro")

personagem1.receber_dano(80)
personagem1.curar(60)
personagem1.subir_nivel()
personagem1.status()
print("\n")
personagem2.receber_dano(100)
personagem2.curar(150)
personagem2.status()