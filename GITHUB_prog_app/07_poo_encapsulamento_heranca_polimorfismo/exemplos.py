# 1. Encapsulamento - proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # Privado: dois sublinhados

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.salario:.2f}")

    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0 or porcentagem > 50:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")

    def bonus(self):
        return self.salario * 0.10


ana = Funcionario("Ana", 3000)
ana.apresentar()
ana.dar_aumento(10)
ana.apresentar()

try:
    # try/except é um bloco usado em programação para tratar erro
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente.")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora.")

print("\n\n\n\n\n")

#2. Herança

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe, setor):
        super().__init__(nome, salario) #super() chama o construtor da classe mãe
        self.equipe = equipe #atributo novo
        self.setor = setor

    def mostrar_equipe(self):
        print(f"{self.nome} gerencia uma equipe de {self.equipe} pessoas, no setor de {self.setor}.")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def mostrar_curso(self):
        print(f"{self.nome} faz curso de {self.curso}.")

Diego = Gerente("Diego", 8000, 20, "SPM")
Caio = Estagiario("Caio", 1500, "Administração comercial")

ana.apresentar()
print("\n")
Diego.mostrar_equipe()
Diego.apresentar()
Diego.dar_aumento(20)
print("\n")
Caio.mostrar_curso()
Caio.apresentar()
Caio.dar_aumento(200)

#3. Polimorfismo
# O mesmo metodo pode existir em várias classes, mas apresentar comportamentos diferentes dependendo do objeto que está sendo executado nesse metodo

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def bonus(self):
        return self.salario * 0.20 + self.equipe * 100


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def bonus(self):
        return 200

print("\n\n\n====== Polimorfismo =====\n")
#Criando objetos de diferentes classes
equipe = [
    Funcionario("Ana", 3000),
    Gerente("Bruno", 8000, 5),
    Estagiario("Caio", 1500, "Análise de Sistemas")
]
#Percorrendo a lista funcionário
for funcionario in equipe:
    print(f"{funcionario.nome}: R$  {funcionario.bonus()}")