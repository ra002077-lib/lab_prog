

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    
    if numero == 0:
        print("Programa encerrado.")
        break
    if numero >=10 and numero <= 50:
        print("Dado Válido")
    else:
        print("Dado Inválido")
