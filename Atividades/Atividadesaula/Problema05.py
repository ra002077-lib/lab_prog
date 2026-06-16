numeros = []

for i in range(6):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

x = int(input("\nDigite o número (X): "))

ocorrencia = numeros.count(x)
print("-"*30)
print(f"O número {x} aparece {ocorrencia} vez(es) na lista.")

if ocorrencia > 0:
    indice = numeros.index(x)
    print(f"A primeira ocorrência do número {x} está no índice {indice}.")
else:
    print(f"O número {x} não foi encontrado na lista.")
    