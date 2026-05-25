import random

lancamentos = []
contador = 0
total = 100

for _ in range(total):
    resultado = random.randint(1, 6)
    lancamentos.append(resultado)
    
    if resultado == 6:
        contador += 1


print(f"Vetor gerado: {lancamentos}")
print(f"Total de faces 6: {contador}")
