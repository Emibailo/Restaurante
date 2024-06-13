# 1 criar uma classe Restaurante usando construtor
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    # 4 criar método para listar os restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# 2 criação de objetos
restaurante_praca=Restaurante('Praça','Gourmet')

restaurante_pizza=Restaurante('Pizza Express','Italiana')




# 3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# 5 consumindo o método listar_restaurantes
Restaurante.listar_restaurantes()


