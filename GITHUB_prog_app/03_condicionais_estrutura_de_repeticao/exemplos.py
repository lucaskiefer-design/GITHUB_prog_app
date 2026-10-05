#1. Estrutura Condicionais

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# 2. Condicionais e Operadores Lógicos
#and -> Todas as condições devem ser verdadeiras
#or -> Pelo menos uma condição deve ser veradeira
#not -> Inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada Permitida")
else:
    print("Entrada não permitida")

    #3. Estrutura de Repetição while

    while contador <= 5:
        print(contador)
        contador += 1

        #4. Estrutura de Repetição for
        for numero in range(1,6):
            print(numero)

            #5. Percorrendo uma lista
            nome = ["Ana", "Carlos", "João", "Maria"]

            for nome in nomes:
                print(nome)

                #6. Break, Continue, Pass

                for numero in range(1,11):

                    if numero == 6:
                        #break
                        #continue
                        #pass
                        print(numero)

