# Aluno: Joao Victor Benedet Machado        
# Turma: 2190
# Data: 27/08/2024

MainDict = {}   # Criei o dicionario principal


def ShowMenu():   # funcao para mostrar o menu
    print(""" 
Menu de Opções:
          
    C - Cadastrar 
    A - Alterar
    E - Excluir
    P - Pesquisar
    S - Sair       
""")
    
def LastPosition(dic):  # funcao para sempre pegar a ultima posicao e somar +1 assim evitando sempre possiveis confilitos 
    NovaLista = list(dic)
    if NovaLista == []:
        return 1
    else: 
        UltimaPos = NovaLista[-1:]
        Numero = UltimaPos[0]
        return Numero + 1


def Cadastrar(pos, nome, cargo):  # cadastra atraves da pos, nome e cargo no maindict
    MainDict[pos] = [nome, cargo]
    print(f"Usúario {nome} de função {cargo} integrado ao ID {pos}")


def Alterar(pos):  # altera atraves da posicao, caso nao esteja ali, daa erro
    if pos not in MainDict.keys():
        print("ERRO! Posição não encontrada!")
    else:
        escolha = input("voce deseja alterar o 1 = nome ou 2 = cargo? digite 1 ou 2: ")
        if escolha == '1':
            novo_nome = input("Digite o novo nome: ")
            MainDict[pos][0] = novo_nome  
            print("nome alterado!")
        elif escolha == '2':
            novo_cargo = input("Digite o novo cargo: ")
            MainDict[pos][1] = novo_cargo 
            print("cargo alterado!")
        else:
            print("opção invalida!")



def Excluir(pos):  # caso nao tenha o pos ali, da erro, se tem, ele exclui normalmente
    if pos not in MainDict.keys():
        print("ERRO! Posicao nao encontrada! ")
    else: 
        del MainDict[pos]
        print(f"Posição {pos} Excluida")


def Pesquisar(dic):   # associa uma lista ao dicionario para conseguir ter os valores das keys
    NovaListaTotal = list(dic)
    NovaListaFunc = []  # cria uma lista para armazenar os funcionarios e os cargos atraves do 'for' 
    Total = len(NovaListaTotal)
    for pos, lista in dic.items():
        NovaListaFunc.append(lista)
    NovaListaFunc.sort()  #organiza alfabeticamente
    print(f"Total Adcionados: {Total}")
    for i, o in NovaListaFunc:
        print(f"{i} | {o}")  # mostra o nome e a sua funcao correspondente


while True:
    ShowMenu()  # mostra o menu

    escolha = str(input("> ")).upper() # pede a opcao ao usuario
 
    if escolha == "C": # se escolha igual a c, ele pede o nome, cargo e chama a funcao LastPosition() para declarar a posicao
        nome = str(input("Digite o Nome Do Funcionario: ")).title() 
        cargo = str(input("Digite o Cargo: ")).title()
        pos = LastPosition(MainDict)
        Cadastrar(pos, nome, cargo) # envia para a funcao

    elif escolha == "A": # parecido com a de cima, porem aqui ele pede a posicao, nao associa a funcao
        pos = int(input("Que Posição Desejas alterar?: "))
        Alterar(pos)
    
    elif escolha == "E":  # pede somente a posicao para excluir
        pos = int(input("Que Posição Desejas excluir?: "))
        Excluir(pos)  # e exclui com a funcao correspondente
    
    elif escolha == "P": 
        Pesquisar(MainDict)  # se escolha igual a 'P', ele simplesmente chama sua funcao
    
    elif escolha == "S":  # sai do programa
        print("Saindo Do Programa...")
        exit()

 
    elif escolha not in ("C", "A", "E", "P", "S"):  # caso nao esteja de acordo com a tupla com as possiveis opcoes, da erro e retorna o while
        print("ERROR! Função nao encontrada! Tente Novamente")



