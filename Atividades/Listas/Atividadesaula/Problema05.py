lista = 5
numeros = []
x = 0

for i in range(lista):
    numeros.append(input(f"Número  {i+1}: "))
    x.append(float(input(f"Nota de {numeros[i]}: ")))
    