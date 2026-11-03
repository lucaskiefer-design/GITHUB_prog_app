class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        soma = 0
        for produto in self.itens:
            soma += produto.subtotal()
        return soma

    def mostrar(self):
        print("=== CARRINHO DE COMPRAS ===")
        for produto in self.itens:
            print(f"{produto.nome} | {produto.quantidade} x R$ {produto.preco:.2f} "
                  f"= R$ {produto.subtotal():.2f}")
        print("---------------------------")
        print(f"TOTAL DA COMPRA: R$ {self.total():.2f}")


p1 = Produto("Arroz 5kg", 28.90, 2)
p2 = Produto("Feijão 1kg", 8.50, 3)
p3 = Produto("Leite", 5.99, 6)
p4 = Produto("Café 500g", 17.80, 1)

carrinho = Carrinho()
carrinho.adicionar(p1)
carrinho.adicionar(p2)
carrinho.adicionar(p3)
carrinho.adicionar(p4)
print("\n")
carrinho.mostrar()