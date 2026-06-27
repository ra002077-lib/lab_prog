# Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto
distância = float(input("Digite a distância em km:  "))
consumo_médio = float(input("Digite o consumo_médio em lt/km:  "))
consumo_total = distância // consumo_médio
print(f"consumo_total é {consumo_total}")