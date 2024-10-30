class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def mark(self):
        self.status = True
    
    def show(self):
        status = "✓" if self.status else "✗"
        print(f"Задача: {self.name} - {status}")

def load_from_file(filename):
    #TO-DO: проверить, существует ли файл, чтобы не встретить ошибку при работе программы 
    tasks = []
    with open(filename, 'r') as file:        
        for line in file:
            task, status = line.strip().split(";")
            tasks.append(Task(task, status))
    return tasks
  

def show_tasks(tasks):
    if not tasks:
        print("Нет задач!")
    else:
        print("\nСписок задач:")
        for task in tasks:
            task.show()


def save(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:         
            file.write(f"{task.name};{task.status}\n")


def add_task(tasks, task):
    tasks.append(Task(task, False))
    return tasks


def mark_comleted(tasks, number):
    # Проверить, что задача с номером, который ввел пользователь, есть в списке
    if number < len(tasks):
        # Изменить статус у задачи с нужным номером
        tasks[number].mark()
    # Вернуть обновленный список
    return tasks


tasks = load_from_file("tasks.txt")

while True:
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Выйти и сохранить задачи")
    choice = input("Выбери действие (1-4): ")
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        task = input("Введите задачу: ")
        tasks = add_task(tasks, task)
    #TO-DO: Создать и вызвать функцию для отметки выполненной задачи  
    elif choice == "3":
        #TO-DO: добавить проверку
        number = int(input("Введите номер задачи для отметки выполнения: ")) - 1
        tasks = mark_comleted(tasks, number)
    elif choice == "4":
        save(tasks, "tasks.txt")
        print("Задачи сохранены. До свидания!")
        break
    else:
        print("Какая-то ошибка, неверный ввод!")    
