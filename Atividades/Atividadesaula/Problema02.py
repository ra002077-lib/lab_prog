numero = int(input("Digite um número inteiro positivo: "))
produto = 1

for i in range(1, numero + 1, 2):
    produto *= i
    print(f"Multiplicando por {i}, resultado atual: {produto}")

print(f"Resultado final: {produto}")