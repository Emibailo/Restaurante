import os 

# restaurantes = ['Funeraria e Pizzaria Dona Lucia','Tokomia','Saburov']
# dicionario
restaurantes=[{'nome':'Pão com Banha','categoria':'gourmet','ativo':False},
              {'nome':'Saco do Feijão','categoria':'feijoada','ativo':True},
              {'nome':'Bife Sujo','categoria':'churrascaria','ativo':False}]


def exibir_maracutaia():
    print('''██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀\n''')

def definir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair \n')

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()

def opc_invalida():
    print('opção invalida \n')
    voltar_menu()

def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar um novo restaurante
     
       Inputs:
       -Nome do restaurante
       -Categoria
       
       Outputs:
       - Adiciona um novo restaurante ao dicionário restaurantes
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante ={'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        ativo= 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu()
    
def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante\n')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado')
    
    voltar_menu()
        
def fechar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system('cls')
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opcoes():
    try:
        opc_escolhida = int(input("Escolha uma opção: "))

        if opc_escolhida==1:
            cadastrar_novo_restaurante()
        elif opc_escolhida==2:
            listar_restaurantes()
        elif opc_escolhida==3:
            print('Ativar Restaurante')
            alterar_estado_do_restaurante()
        else:
            fechar_app()
    except:
        opc_invalida()

def main():
    os.system("cls")
    exibir_maracutaia()
    definir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()


# add 
    
# 3 importar o arquivo que contém a classe Restaurante
from modelos.restaurante4 import Restaurante

# 4 criar um objeto(instância de Restaurante)
restaurante_praca=Restaurante('praça','gourmet')
restaurante_mexicano=Restaurante('mexican food','mexicana')
restaurante_japones=Restaurante('japa','japonesa')


# alternar estado de um restaurante
restaurante_japones.alternar_estado()


# criando avaliações para o restaurante praça
restaurante_praca.receber_avaliacao('Albino',8)
restaurante_praca.receber_avaliacao('Berenice',5.5)




# 2 criando a chamada da função de entrada
def main():
    # 5 inserir uma ação dentro do main
    Restaurante.listar_restaurantes()
    

if __name__=='__main__':
    main()