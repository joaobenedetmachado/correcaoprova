#Aluno: João Victor Benedet Machado
#Turma: 2190
#Data : 17/09/2024

dicPedidos = {} # Cria o dicionario principal


def MostrarPedidos(dicionario): # Mostra os pedidos de forma organizada com for's
    for i, o in dicionario.items():
        print(f"{i}")
        print('Pedidos: ')
        for x in o:
            print('   ',x)

def ShowMenu(): # Um print para mostrar o menu
    print(""" 
    1) Adcionar Pedidos
    2) Atualizar Pedido
    3) Remover Pedidos
    4) Filtrar Pedidos Por Cliente
    5) Visualizar Pedidos
    6) Sair
    """)

def AdcionarPedido(nome, lista): # Funcao para adcionar no dicionario principal
    dicPedidos[nome] = lista
    print(dicPedidos)


def AtualizarPedido(nome, prato, pratonovo): # Checa se ha nas chaves, se nao tem, printa erro
    if nome in dicPedidos.keys() and prato in dicPedidos[nome]:
        lista = dicPedidos[nome]
        for i in range(len(lista)):
            if lista[i] == prato:
                lista[i] = pratonovo  
                dicPedidos[nome] = lista  
                print(f'prato "{prato}" alterado para "{pratonovo}" com sucesso')
                return 
    else:
        print("ERROR! usuario ou prato nao encontrado!")


def ExcluirPrato(nome, prato):
    if nome in dicPedidos.keys() and prato in dicPedidos[nome]:
        lista = dicPedidos[nome]
        for i in range(len(lista)):
            if lista[i] == prato:
                lista.pop(i)  
                dicPedidos[nome] = lista  
                print(f'prato "{prato}" removido com sucesso')
                return 
    else:
        print("ERROR! usuario ou prato nao encontrado!")



def FiltrarPedidos(nome): # ve se tem o nome nos pedidos/dicionario, caso nao mostra erro
    if nome in dicPedidos.keys():
        for i in dicPedidos[nome]:
            print(f"PEDIDOS: {i}")
    else:
        print("ERROR! usuario não encontrado!")

while True: # enquanto o while nao quebrar ele faz isso:
    ShowMenu()
    escolha = int(input("> "))

    if escolha == 1: # pergunta o nome, cria uma lista, e um while para o user adcionar quantos pedidos quiser
        nome = input("Qual seu nome: ")
        listaPedidos = []
        while True:
            pedido = input('Qual seu pedido: ')
            listaPedidos.append(pedido)
            escolha = input("Deseja Continuar: ").lower()
            if escolha == 'n':
                AdcionarPedido(nome, listaPedidos)
                break
            else:
                continue

    if escolha == 2:
        nome = input("Nome do usuario para alterar os pratos: ") # pergunta o nome, cria a lista, igual a de cima, porem aqui a funcao chamada é outra
        while True:
            pedido = input('Qual seu pedido que deseja alterar: ')
            pratonovo = input('Deseja alterar para: ')
            escolha = input("Deseja Continuar: ").lower()
            if escolha == 'n':
                AtualizarPedido(nome, pedido, pratonovo)
                break
            else:
                continue
            
    if escolha == 3: # pergunta o nome e o prato para excluir, e chama a funcao
        nome = input("Nome do usuario para excluir certo prato: ")
        prato = input("Prato que deseja excluir: ")
        ExcluirPrato(nome, prato)

    if escolha == 4: # pergunta o nome e chama a função
        nome = input("Nome do usuario para encontrar pratos: ")
        FiltrarPedidos(nome)

    if escolha == 5: # chama a funcao
        MostrarPedidos(dicPedidos)

    if escolha == 6: # sai do programa, o break tambem funcionaria
        print("Saindo do programa...")
        exit()

        

        
print(dicPedidos)