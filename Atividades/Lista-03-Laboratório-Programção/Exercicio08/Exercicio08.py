x = int(input("Digite o Valor de (x): "))
y = int(input("Digite o Valor de (y): "))

quociente = 0
resto = x

while resto >= y:
    resto -= y
    quociente += 1

print(f"\nResultado da divisão: {quociente}")
print(f"Resto da divisão: {resto}")