n = int(input("Digite um número inteiro: "))

if n <= 0:
    print("Digite um número maior que zero: ")
else:
    print(f"Sequência de Collatz para {n} é: ")
    print(n, end=" ")
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2  
        else:
            n = 3 * n + 1 
        
        print(f"→ {n}", end=" ")
    
    print("\nFim da sequência!")