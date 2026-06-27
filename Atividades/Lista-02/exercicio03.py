def calcular_frete():
    print("--- Cálculo de Frete ---")
    
    distancia = float(input("Informe a distância total (km): "))
    peso = float(input("Informe o peso do pacote (kg): "))
    
    valor_frete = 0.0

    if distancia > 100:
        km_extra = distancia - 100
        valor_frete += 20 + (km_extra * 0.10)
    else:
       valor_frete += 20 

    if peso > 10:
        kg_extra = peso - 10
        valor_frete += kg_extra * 5

  
    print("\n--- Resumo do Frete ---")
    print(f"Distância percorrida: {distancia} km")
    print(f"Peso do pacote: {peso} kg")
    print("-" * 23)
    print(f"Valor Total do Frete: R$ {valor_frete:.2f}")


calcular_frete()