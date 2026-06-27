import random

num_secreto = random.randint(1, 100)
num_tentativas = 0
max_tentativas = 10

while num_tentativas < max_tentativas:
    tentativa = int(input(f"\nTentativa {num_tentativas + 1} / {max_tentativas} Digite seu número: "))
    
    
    if tentativa < 1 or tentativa > 100:
        print("NÚMERO INVÁLIDO! Digite um valor entre 1 e 100.")
        
        
    else:
        
        num_tentativas += 1
        
        if tentativa == num_secreto:
            print("PARABÉNS! VOCÊ ACERTOU!!!")
            if num_tentativas < 5:
                print("VOCÊ GANHOU UM BÔNUS!")
            break
        elif tentativa < num_secreto:
            print("Número mais Alto. Tente novamente.")
        else:
            print("Número mais Baixo. Tente novamente.")
            
else:
    print(f"\nVocê esgotou suas {max_tentativas} tentativas.")
    print(f"O número secreto era: {num_secreto}. Até a próxima!")    
    
    
     
   
