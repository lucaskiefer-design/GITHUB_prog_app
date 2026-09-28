#Listas, Tuplas e Dicionarios
from operator import index

#1 Listas
#Listas são utilizadas para armazenar vários valores
#Dentro de uma variável
nomes=["Ana" , "Carlos" , "João" , "Maria"]
print(nomes)

#2 Acessando elementos da Lista
print(nomes[0])
print(nomes[1])
#Podemos acessar o ultimo elemento usando -1
print(nomes[-1])

#3 Alterando elementos
#As listas são mutáveis, ou seja, os elementos podem ser alterados
nomes[0] = "Pedro"
print(nomes)

#4 Adicionando elementos no final da lista
nomes.append("Lucas")
print(nomes)
#Insert() adiciona um elemento em uma posição
nomes.insert(1, "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() remove o elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)
#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)

#6. Tamanho da Lista
#len() Informa a quantidade de elementos
print(len(nomes))

# 7. Percorrendo uma Lista
for nome in nomes:
    print(nome)
#8. Verificando se um elemento existe
if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")

# 9. Lista com Diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)
