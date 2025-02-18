def calcular_desconto(valor_total, valor_desconto):
    desconto = valor_total * valor_desconto / 100
    valor_com_desconto = valor_total - desconto
    return valor_com_desconto


resultado_1 = calcular_desconto (1000,15)
print(resultado_1)



