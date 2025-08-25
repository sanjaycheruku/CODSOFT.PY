# Simple To-Do List Application

tasks = []  # empty list to store tasks

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
