from time import sleep
import os

def criarTarefa(lista):
    """
    _
    """
    tarefa = {}
    tarefa["nome"] = input("Digite o nome da tarefa:")
    tarefa["prioridade"] = input("Digite a prioridade da tarefa:(alta/media/baixa)")
    tarefa["categoria"] = input("Digite a categoria da tarefa: (domestica/lazer/corporativa)")
    lista.append(tarefa)
    print("\033[32mTarefa adicionada com sucesso\033[m")
    sleep(5)
    os.system("cls")

def marcarConcluida():
    pass 

def listar(lista):
    for tarefa in lista:
        for chave,valor in tarefa.items():
            print(f"{chave}:{valor}")
        print("="*40)
    
def removerTarefa(lista):
    nome = input("Digite o nome da tarefa")
    for tarefa in lista:
        if tarefa["nome"] == nome:
            lista.remove(tarefa)
            print("\033[31mTarefa Excluída com sucesso!\033[m")

            break
    return "Tarefa não encontrada"


    lista.remove(nome)
def listarporCategoria(lista):
    categoria = input("Digite o nome da categoria:(lazer/domestica/corporativo)")
    for tarefa in lista:
        if tarefa["categoria"] == categoria:
            for chave,valor in tarefa.items():
                print(f"{chave}:{valor}")
            print("="*40)

def listarporPrioridade():
    pass


def menu():
    print("="*30)
    print("Gerenciador de Tarefas".center(30))
    print("="*30)
    print("1 - Para adicionar")
    print("2 - Para listar")
    print("3 - Para excluir")
    print("4 - Para sair")
    op:int = int(input("->"))
    return op

def menuFiltro():
    print("="*30)
    print("Filtro de Tarefas".center(30))
    print("="*30)
    print("1 - Filtrar por categoria")
    print("2 - Para Prioridade")
    print("3 - Geral")
    print("4 - Sair")