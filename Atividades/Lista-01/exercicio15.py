def calcular_moedas(valor):
    moedas = [100, 50, 25, 10, 5, 1]  
    quantidade_moedas = []

    for moeda in moedas:
        quantidade = valor // moeda 
        valor %= moeda  
        quantidade_moedas.append(quantidade)

    return quantidade_moedas


valor_centavos = int(input("Digite o valor em centavos: "))

quantidade_moedas = calcular_moedas(valor_centavos)

print(f"Quantidade de moedas para {valor_centavos} centavos:")
nomes_moedas = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos", "1 centavo"]
for i in range(len(quantidade_moedas)):
    if quantidade_moedas[i] > 0:
        print(f"{quantidade_moedas[i]} moeda(s) de {nomes_moedas[i]}")