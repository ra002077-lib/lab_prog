while True:
    num = int(input("\nDigite um número inteiro positivo: "))
    qtde_divisores = 0
    print(f"Divisores de {num}: ", end= " ")
    for i in range(1, num+1):        
        if num%i == 0:    
            print(i, end=" ")
            qtde_divisores += 1

    print()
    if qtde_divisores == 2:
       print(f"Conclusão: O número {num}  é primo")
    else:
       print(f"Conclusão: O número {num} não é primo (Possui {qtde_divisores} divisores)")
    continuar=input("\nDeseja analisar outro número?(S/N): "). upper()
    if continuar != 'S':
       break