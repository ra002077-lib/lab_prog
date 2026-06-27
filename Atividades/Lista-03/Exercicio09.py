a = int(input("Digite o valor inicial (a): "))
b = int(input("Digite o valor final (b): "))

soma = 0
lista_impares = []

for i in range(a, b + 1):
    if i % 2 != 0:
        soma += i
        lista_impares.append(i)

print(f"Números ímpares encontrados: {lista_impares}")
print(f"A soma de todos eles é: {soma}")