senha_correta = "6184"

for tentativa in range(1, 4):
    senha_digitada = input(f"Tentativa {tentativa} de 3 - Digite a senha: ")
    
    if senha_digitada == senha_correta:
        print("Acesso Permitido")
        break 
    else:
        print("Senha incorreta.")
else:

    print("Acesso Bloqueado")