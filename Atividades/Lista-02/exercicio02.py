def calcular_valor_final():
    print("--- Sistema de Descontos ---")
    
    tipo_cliente = input("Informe o tipo de cliente (comum, premium ou vip): ").strip().lower()
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if tipo_cliente == "premium":
        desconto = 0.10  
    elif tipo_cliente == "vip":
        desconto = 0.20  
    elif tipo_cliente == "comum":
        desconto = 0.00  
    else:
        print("Tipo de cliente inválido. Considerando como 'comum'.")
        desconto = 0.00

    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto

    print("\n--- Resumo do Pedido ---")
    print(f"Tipo de Cliente: {tipo_cliente.capitalize()}")
    print(f"Valor Original: R$ {valor_compra:.2f}")
    print(f"Desconto Aplicado: R$ {valor_desconto:.2f} ({desconto * 100:.0f}%)")
    print("-" * 25)
    print(f"Valor Final: R$ {valor_final:.2f}")

calcular_valor_final()