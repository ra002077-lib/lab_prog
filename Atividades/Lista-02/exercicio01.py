def validar_senha():
    print("--- Validar de Senha ---")
    senha = input("Digite sua senha: ")

    qtd_caracteres = len(senha) >= 8
    numero = False
    letra = False

    for caractere in senha:
        if caractere.isdigit():
            numero = True
        elif caractere.isalpha():
            letra = True

    print("\nRelatório de Validação:")
    
    if qtd_caracteres:
        print("Pelo menos 8 caracteres: OK")
    else:
        print("Pelo menos 8 caracteres: Faltou")

    if numero:
        print("Contém pelo menos um número: OK")
    else:
        print("Contém pelo menos um número: Faltou")

    if letra:
        print("Contém pelo menos uma letra: OK")
    else:
        print("Contém pelo menos uma letra: Faltou")

    
    if qtd_caracteres and numero and letra:
        print("\nSenha válida! ")
    else:
        print("\nSenha Inválida! ")

validar_senha()