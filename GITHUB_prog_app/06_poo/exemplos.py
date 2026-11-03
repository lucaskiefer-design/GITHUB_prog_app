#1. Classe: o modelo (planta)

class Celular:
    def __init__(self, marca, modelo, cor, bateria = "100%"):
        #Atributos: as características do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#4. Metodos: o comportamento do objeto
    def ligar(self):
        # O metodo consulta um atributo do próprio objeto
        if self.bateria == "0%":
            print("Sem bateria! Coloque o celular para carregar!")
        else:
            self.ligado = True
            print("Ligado!")

    def desligar(self):
        self.ligado = True
        print("Desligado!")

#5. Objetos: Criados a partir da classe (as casas)
celular1 = Celular("Samsung", "Galaxy S23", "Azul")
celular2 = Celular("Apple", "IPhone 17", "Amarelo", "0%")

#6. Acessando e alterando atributos
#Usamos objeto.atributo

print(celular1.marca)
print(celular1.bateria)
print(celular2.bateria)

#7. Chamando metodos
#Usamos objeto.metodo() para pedir que o objeto faça algo

celular2.ligar()