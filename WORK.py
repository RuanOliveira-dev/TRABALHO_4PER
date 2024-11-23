#LISTA
lista_alunos = [] #matriz unidirecional (vetor) linha com colunas

#FUNÇÃO
def cadastrar():
    adicionar_aluno = input("Digite o nome do aluno: ")
    lista_alunos.append(adicionar_aluno)
    print(f"O aluno {adicionar_aluno} foi inserido com SUCESSO!")
    print(lista_alunos)
    
def remover():
    remover_aluno = input("Digite o nome do aluno que queres remover: ")
    lista_alunos.remove(remover_aluno)
    print(f"O aluno {remover_aluno} foi removido com SUCESSO!")
    print(lista_alunos)

def atualizar():
    print(lista_alunos)
    aluno_buscado = int(input("Digite a posição do aluno que queres atualizar: "))
    new_name = input("Digite o novo nome do aluno: ")
    lista_alunos[aluno_buscado] = new_name
    print(f"O aluno {new_name} foi atualizado com SUCESSO!")
    print(lista_alunos)

def ler():
    print(f"A lista atual está {lista_alunos}")

def menu():
    while True:
        print("SISTEMA DE ALUNOS")
        print("1 - CADASTRAR UM ALUNO")
        print("2 - ATUALIZAR UM ALUNO")
        print("3 - REMOVER UM ALUNO")
        print("4 - LISTAR OS ALUNOS")
        print("5 - SAIR DO PROGRAMA")
        opcao = int(input("Digite uma das opções: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            atualizar()
        elif opcao == 3:
            remover()
        elif opcao == 4:
            ler()
        elif opcao == 5:
            print("Saindo do programa... Tchau tchau")
            break
        else:
            print("Valor inválido! ")        
menu()