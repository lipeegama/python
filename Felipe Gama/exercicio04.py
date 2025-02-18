def celsius_para_fahrenheit (celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius_1 = float(input('Digite a temperatura em Celsius: '))
valor_fahrenheit = celsius_para_fahrenheit(celsius_1)
print(f'Temperatura em Fahrenheit: {valor_fahrenheit}')

    
