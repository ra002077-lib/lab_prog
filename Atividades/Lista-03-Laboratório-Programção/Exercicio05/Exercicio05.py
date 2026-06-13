n_desejado = int(input("Quantos números perfeito você deseja encontrar? "))
encontrados = 0
numero_testado = 2 
print(f"Buscando os {n_desejado} primeiro números perfeitos")
while encontrados < n_desejado:
    soma_divisores = 0    
    for i in range(1, numero_testado):
        if numero_testado % i == 0:
            soma_divisores += i

    
    if soma_divisores == numero_testado:
        encontrados += 1
        print(f"{encontrados} ° número perfeito encontrado: {numero_testado}") 

    numero_testado += 1