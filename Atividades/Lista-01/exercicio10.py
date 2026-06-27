import math

def calcular_distancia():
    print("--- Calculadora de Distância entre Dois Pontos ---")    

    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))
    
    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))    

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)    
    
    print(f"\nA distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia:.2f}")

if __name__ == "__main__":
    calcular_distancia()