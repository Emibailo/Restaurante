# 1 criar uma classe Restaurante
class Restaurante:
    nome=''
    categoria='churrascaria'
    ativo=False

# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()
# questão 1

restaurantes=[restaurante_praca,restaurante_pizza]

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))

# QUESTÃO 1
restaurante_praca.categoria='Italiana'
print(restaurante_praca.categoria)
print('')

# QUESTÃO 2
nome_restaurante=restaurante_praca.nome
print(nome_restaurante)
print('')

# QUESTÃO 3
if restaurante_praca.ativo:
    print('O resturante está ativo')
else:
    print('O restaurante está inativo')
print('')

#QUESTÃO 4
categoria=Restaurante.categoria
print(categoria)
print('')

# QUESTÃO 5
restaurante_praca.nome='Bistrô'
print(restaurante_praca.nome)
print('')

#   QUESTÃO 6
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
print(vars(restaurante_pizza))
print('')

# QUESTÃO 7
if restaurante_pizza.categoria=='Fast Food':
    print('A categoria é fast food')
else:
    print('A categoria não é fast food')

print('')

# QUESTÃO 8
restaurante_pizza.ativo=True
print(restaurante_pizza.ativo)
print('')

# QUESTÃO 9
print(f'Nome: {restaurante_praca.nome} e a categoria: {restaurante_praca.categoria}')


