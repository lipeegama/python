def verificar_idade(idade):
    if idade >= 18:
        mensagem = 'Maior de idade'
    else:
        mensagem = 'Menor de idade'
    return mensagem

print(verificar_idade(78))
print(verificar_idade(12))