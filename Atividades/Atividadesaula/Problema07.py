pares = []
impares = []
print("Digite 10 números inteiros: ")
while len(pares) + len(impares) < 10:
    num = int(input("Número: "))
    if num in pares or num in impares:
        print(" Esse número já foi inserido digite um número diferente.")
        continue
    if num % 2 == 0:
        pares.append(num)
        print(f"-> {num} adicionados aos Pares.")
    else:
        impares.append(num)
        print(f"-> {num} adicionado aos Impares.")
    
print("\n--- Resultado Final ---")
print(f"Lista de Pares: {pares}")
print(f"Lista de Impares: {impares}")

