class Restaurante:
    nome=""
    categoria = 'Italiana'  # Exercício 1
    ativo=False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'gourmet'

restaurante_pizza = Restaurante()

restaurantes=[restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))

# Exercício 2
nome_restaurante=restaurante_praca.nome
print(nome_restaurante)

# Exercício 3
if restaurante_praca.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")

# Exercício 4
categoria = Restaurante.categoria

# Exercício 5
restaurante_praca.nome = 'Bistrô'

# Exercício 6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food' 

# Exercício 7
if restaurante_pizza.categoria == 'Fast Food':
    print("A categoria de restaurante_pizza é 'Fast Food'.") 

# Exercício 8
restaurante_pizza.ativo = True

# Exercício 9
print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")
