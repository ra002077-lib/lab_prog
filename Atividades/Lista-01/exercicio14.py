valor_original = float(input("Digite o valor da roupa: R$"))

desconto = valor_original * 0.30
valor_com_desconto = valor_original - desconto

print(f"O valor da roupa com 30% de desconto é: R${valor_com_desconto:.2f}")