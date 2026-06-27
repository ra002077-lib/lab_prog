def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius *1.8 + 32
    return fahrenheit

temp_c = float(input("Digite a Temperatura em graus celsius: "))
temp_f = celsius_para_fahrenheit(temp_c)

print(f"{temp_c} °C é igual a {temp_f}°F")