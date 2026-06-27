n_termos = int(input("Quantos termos da série Fibonacci deseja ver? "))

a, b = 0, 1
contador = 0 
print("Sequencia de Fibonacci")
while contador <= n_termos:
    print(a,end=", " if contador < n_termos else "")

    proximo = a + b
    a = b
    b = proximo
    contador += 1

