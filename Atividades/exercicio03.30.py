import random

lancamentos = []
contador_seis = 0
total = 50

for _ in range(total):
    resultado = random.randint(1, 6)
    lancamentos.append(resultado)
    
    if resultado == 6:
        contador_seis += 1


porcentagem = (contador_seis / total) * 100

print(f"Vetor gerado: {lancamentos}")
print(f"Total de faces 6: {contador_seis}")
print(f"Porcentagem: {porcentagem:.2f}%")