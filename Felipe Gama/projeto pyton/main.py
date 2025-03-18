# ENTRADA 
# Type hint ---> dica de tipo
import funcoes 
from funcoes import *# IMPORTA TUDO DO ARQUIVO FUNCOES
lista_tarefas = [
    {
        "nome":"Varre casa" ,
        "prioridade":"Alta",
        "categoria":"domestica"
    },
    
    {
        "nome":"Estudar Django" ,
        "prioridade":"Alta",
        "categoria":"Lazer"
    },
    {
        "nome":"Lavar Vasilha" ,
        "prioridade":"Media",
        "categoria":"domestica"
    },
    {
        "nome":"Estudar Next.js" ,
        "prioridade":"baixa",
        "categoria":"lazer"
    },
    {
        "nome":"Dar uma aula de datascience" ,
        "prioridade":"Alta",
        "categoria":"corporativa"
    },
    {
        "nome":"Assistir um filminho com a morena(cremosa)" ,
        "prioridade":"Alta",
        "categoria":"lazer"
    },

    
]
# PROCESSAMENTO




while True :
    op = funcoes.menu()
    if op == 1:
        funcoes.criarTarefa()
    if op == 2:
        op2 = funcoes.menuFiltro()

        if op2 == 1:
            listarporPrioridade()
        
        if op2 == 2:
            funcoes.listarporCategoria()
        if op2 == 3:
            funcoes.listar()

        if op2 == 4:
            break

    if op == 3:
        funcoes.removerTarefa()
    if op == 4:
        break
