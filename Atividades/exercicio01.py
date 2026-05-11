vetor = []
print("Digite 10 valores: ")
for i in range(10):
    soma = input(f"Digite o {i + 1}° valor: ")
    vetor.append(soma)
val_dif = []
for num in vetor:
    if num not in val_dif:
        val_dif.append(num)

quantde = len(val_dif)

print(f"Valores digitados: {vetor}")
print(f"Existem {quantde} valores diferentes no vetor.")
            

    
