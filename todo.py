#!/usr/bin/env python3
import sys
import os

def load_tasks(filename="tasks.txt"):
    """Загружает список задач из файла. Если файла нет, возвращает пустой список."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        tasks = f.read().splitlines()
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    """Сохраняет список задач в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))

def main():
    if len(sys.argv) < 2:
        print("Использование: python todo.py [list|add|remove|clear] [текст задачи / номер задачи]")
        return

    command = sys.argv[1]
    tasks = load_tasks()

    if command == "list":
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Список задач пуст.")
    elif command == "add":
        if len(sys.argv) < 3:
            print("Использование: python todo.py add \"Текст задачи\"")
            return
        new_task = " ".join(sys.argv[2:])
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Добавлена задача: {new_task}")
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Использование: python todo.py remove <номер_задачи>")
            return
        try:
            task_num = int(sys.argv[2])
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Удалена задача: {removed}")
            else:
                print("Некорректный номер задачи.")
        except ValueError:
            print("Номер задачи должен быть целым числом.")
    elif command == "clear":
        tasks = []
        save_tasks(tasks)
        print("Все задачи удалены.")
    else:
        print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()
