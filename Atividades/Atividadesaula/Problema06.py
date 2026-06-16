nomes = []

for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    nomes.append(nome)

nomes_invertidos = nomes[::-1]

print("\nLista")
print(nomes)

print("\nLista Invertida")
print(nomes_invertidos)