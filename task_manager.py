import os

def load_tasks(file_path):
    """Carrega as tarefas de um arquivo."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def save_tasks(file_path, tasks):
    """Salva as tarefas em um arquivo."""
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    """Adiciona uma nova tarefa."""
    task = input("Digite a nova tarefa: ").strip()
    if task:
        tasks.append(task)
        print(f"Tarefa '{task}' adicionada com sucesso!")

def list_tasks(tasks):
    """Lista todas as tarefas."""
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    file_path = 'tasks.txt'
    tasks = load_tasks(file_path)

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            save_tasks(file_path, tasks)
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
