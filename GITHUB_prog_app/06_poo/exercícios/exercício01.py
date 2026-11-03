#Cachorro

class Cachorro:
    def __init__(self, nome, raca, idade = "10 anos"):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(self.nome , ", diz: Au au!")

    def mostar_info(self):
        print(self.nome)
        print(self.raca)
        print(self.idade)

cachorro1 = Cachorro("Bóris", "Golden")
cachorro2 = Cachorro("Escovão", "Rottweiler", "4 anos")


cachorro1.mostar_info()
cachorro1.latir()
print("\n")
cachorro2.mostar_info()
cachorro2.latir()

print("\n\n")

print(cachorro1.nome)
print(cachorro1.idade)
print(cachorro2.nome)
print(cachorro2.idade)