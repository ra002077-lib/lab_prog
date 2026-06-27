def verificar_rodizio():
    print("--- Consulta de Rodízio ---")
    
    placa = input("Digite a placa do veículo : ").strip()

    if not placa:
        print("Entrada inválida!")
        return

    
    ultimo_digito = placa[-1]

    if ultimo_digito in "12":
        dia = "Segunda-feira"
    elif ultimo_digito in "34":
        dia = "Terça-feira"
    elif ultimo_digito in "56":
        dia = "Quarta-feira"
    elif ultimo_digito in "78":
        dia = "Quinta-feira"
    elif ultimo_digito in "90":
        dia = "Sexta-feira"
    else:
        print(" O último caractere da placa deve ser um número!")
        return

    print(f"\nO veículo de placa final {ultimo_digito} possui rodízio na:")
    print(f" {dia}")


verificar_rodizio()