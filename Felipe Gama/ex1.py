livro = {
    'título': 'Python para Iniciantes',
    'autor': 'João Silva',
    'ano': 2020,
    'editora': 'TechBooks',
}

print(livro['título'])
print(livro['autor'])

print(livro.get('preço'))

print(len(livro))

print('ano' in livro)

livro['preço'] = 49.90
livro['ano'] = 2023

del livro['editora']

livro.clear()
print(livro)