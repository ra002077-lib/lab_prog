moedas_1 = int(input("Digite a quantidade de moedas de 1 centavo: "))
moedas_5 = int(input("Digite a quantidade de moedas de 5 centavos: "))
moedas_10 = int(input("Digite a quantidade de moedas de 10 centavos: "))
moedas_25 = int(input("Digite a quantidade de moedas de 25 centavos: "))
moedas_50 = int(input("Digite a quantidade de moedas de 50 centavos: "))
moedas_1_real = int(input("Digite a quantidade de moedas de 1 real: "))

# Cálculo do valor total em reais
total_centavos = (moedas_1 * 1) + (moedas_5 * 5) + (moedas_10 * 10) + (moedas_25 * 25) + (moedas_50 * 50)
total_reais = total_centavos / 100  # Convertendo centavos para reais
total_reais += moedas_1_real  

print(f"O valor economizado é: R${total_reais:.2f}")