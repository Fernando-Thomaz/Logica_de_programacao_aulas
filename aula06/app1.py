# dicionario com os usuarios
usuario = {
    'nome': 'Fernando',
    'idade': 17,
}

# lista com todos os usuarios
usuarios = ['gomes','andre','maria']

# titulo
print(30*'-','DICIONARIO','-'*30)

# mostra o tipo e o conteudo da variavel
print(type(usuario))
print(usuario)

# mostra o nome do usuario
print(f'Nome: {usuario['nome']}')
print(f'Idade: {usuario['idade']}')

# titulo
print(30*'-','LISTA','-'*30)

# mostra o tipo e o conteudo da variavel
print(type(usuarios))
print(usuarios)

# mostra o nome do usuario
print(f'Nome: {usuarios[0]}')

# adiciona um novo usuario a lista
print(f'Nome: {usuario.get('nome')}')