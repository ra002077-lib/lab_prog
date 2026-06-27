n = int(input("Digite um número para verificar se é produto de 3 consecutivos ")) 
consecutivos = False
i = 1

while i * (i+1) * (i+2) <= n:
    if i * (i+1)*(i+2) == n: 
        print(f"Sim! {n} é o produto de {i}x{i+1}x{i+2}")
        consecutivos = True
        break
    i += 1
if not consecutivos:
    print(f"O número {n} Não é produto de 3 inteiros consecutivos. ")