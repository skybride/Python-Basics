
tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

# NOTE: Order of when function exists to when it's called matters

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")
    save_tasks()

def view_task():
    if not tasks:
        print("No tasks exists")
    else: 
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i} . {task}")

def delete_task():
    view_task()
    try:
        task_num = int(input("Enter number to delete task"))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted!")
            save_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip()) # .strip removes whitespace
        print("Tasks loaded!")
    except FileNotFoundError:
        print("No saved tasks found.")


load_tasks()

while True:
    show_menu()
    choice = input("What do you want to do?")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("")
        break
    else:
        print("Choice not recognized")
