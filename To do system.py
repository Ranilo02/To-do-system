todos = []
categorias = ["Tarefa de Casa", "Tarefas do Trabalho", "Tarefas da Escola"]
from time import sleep

# sim.. no pycharm fica legal
c = (
    "\033[m",  # 0 - sem cores
    "\033[1;35;40m",  # 1 - roxo + fundo preto
    "\033[34m",  # 2 - azul
)


# Função para criar nova to-do
def criar_todo():
    título = input("Digite o título da nova to-do: ")
    listar_categorias()
    categoria = int(input("Digite o número da categoria: ")) - 1
    todo = {"título": título, "concluída": False, "categoria": categorias[categoria]}
    todos.append(todo)
    print(f'To-do "{título}" criada com sucesso!')


# Função para listar todas as categorias disponíveis
def listar_categorias():
    print("Categorias disponíveis:")
    for i, categoria in enumerate(categorias):
        print(f"{i+1}. {categoria}")


# Função para listar todas as to-dos
def listar_todos():
    if len(todos) == 0:
        print("Não há to-dos cadastradas.")
    else:
        for categoria in categorias:
            print(c[2] + f"{categoria}:")
            for i, todo in enumerate(todos):
                if todo["categoria"] == categoria:
                    print(c[1], end="")
                    concluída = "" if not todo["concluída"] else "x"
                    print(f'{i+1}. [{concluída}] {todo["título"]}')
                    print(c[0], end="")


# Função para marcar to-do como concluída
def marcar_concluída():
    listar_todos()
    índice = (
        int(input("Digite o índice da to-do que deseja marcar como concluída: ")) - 1
    )
    todos[índice]["concluída"] = True
    print(f'To-do "{todos[índice]["título"]}" marcada como concluída.')


# Função para excluir to-do
def excluir_todo():
    listar_todos()
    índice = int(input("Digite o índice da to-do que deseja excluir: ")) - 1
    todo_excluída = todos.pop(índice)
    print(f'To-do "{todo_excluída["título"]}" excluída com sucesso!')


# Função para editar título da to-do
def editar_título():
    listar_todos()
    índice = int(input("Digite o índice da to-do que deseja editar o título: ")) - 1
    novo_título = input("Digite o novo título da to-do: ")
    todos[índice]["título"] = novo_título
    print(f"Título da to-do editado com sucesso!")


# Programa principal
sair = 0
while sair == 0:
    print(c[2], end="")
    print("--- MENU ---")
    print("1. Criar to-do")
    print("2. Listar categorias")
    print("3. Listar to-dos")
    print("4. Marcar to-do como concluída")
    print("5. Excluir to-do")
    print("6. Editar título da to-do")
    print("0. Sair")
    opção = int(input("Digite a opção: "))
    print(c[0], end="")
    if opção == 1:
        criar_todo()
    elif opção == 2:
        listar_categorias()
    elif opção == 3:
        listar_todos()
    elif opção == 4:
        marcar_concluída()
    elif opção == 5:
        excluir_todo()
    elif opção == 6:
        editar_título()
    elif opção == 0:
        print("Saindo...")
        sleep(1.5)
        break
    else:
        print("Opção inválida. Tente novamente.")
