quantidade_pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
quantidade_media = int(input("Digite a quantidade de camisetas médias: "))
quantidade_grande = int(input("Digite a quantidade de camisetas grandes: "))

preco_pequena = 10
preco_media = 12
preco_grande = 15

total_arrecadado = (quantidade_pequenas * preco_pequena) + (quantidade_media * preco_media) + (quantidade_grande * preco_grande)

print(f"O valor total arrecadado será: R${total_arrecadado:.2f}")