import random
lancamentos = []
total = 100
contandor = 0
frequencias = [0] * 6

for _ in range(total):
    resultado = random.randint(1, 6)
    lancamentos.append(resultado)

for valor in lancamentos:
    frequencias[valor - 1] += 1
print("Vetor de lançamentos (100 vezes)")
print(lancamentos)
print("\nVetor de Frequências (Quantidade de vezes das faces: 1, 2, 3, 4, 5, 6)")
print(frequencias)
