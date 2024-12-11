from task_tracker import *


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