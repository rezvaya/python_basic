def load_from_file(filename):
    #TO-DO: проверить, существует ли файл, чтобы не встретить ошибку при работе программы 
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            task, status = line.strip().split(";")
            tasks.append({"task": task, "completed": status=="True"})
    return tasks
  

def show_tasks(tasks):
    if not tasks:
        print("Нет задач!")
    else:
        print("\nСписок задач:")
        for task in tasks:
            status = "✓" if task['completed'] else "✗"
            print(f"Задача: {task['task']} - {status}")


def save(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:         
            file.write(f"\n{task['task']};{task['completed']}")


def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    return tasks


tasks = load_from_file("tasks.txt")

while True:
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Выйти и сохранить задачи")
    choice = input("Вебери действие (1-4): ")
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        task = input("Введите задачу: ")
        tasks = add_task(tasks, task)
    #TO-DO: Создать и вызвать функцию для отметки выполненной задачи  
    # elif choice == "3":
    elif choice == "4":
        save(tasks, "tasks.txt")
        print("Задачи сохранены. До свидания!")
        break
    else:
        print("Какая-то ошибка, неверный ввод!")    
