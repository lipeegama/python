produtos ={
    'nome': 'Cafeteria Elétrica',
    'preço': 299.90,
    'marca': 'Philips',
    'estoque': 15,

}

print(f'O estoque do produto é {produtos["estoque"]} unidades.')

produtos['preço'] = produtos['preço'] * 1.15

if produtos['estoque'] > 10:
    print('Produto disponível em grande quantidade')
else:
    print('Estoque baixo')

del produtos['marca']
produtos['descrição'] = 'Cafeteira com 12 opções de preparo de café'

if produtos['preço'] > 300:
    print('Produto caro')
else:
    print('Produto acessível')

print(produtos.get('promoção'))
